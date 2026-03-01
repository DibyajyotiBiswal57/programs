#!/usr/bin/env python3
"""update_changelog.py – Automatically update CHANGELOG.md with new commits/PRs.

Usage:
    python3 update_changelog.py

Environment variables:
    GITHUB_TOKEN        Optional. When set, PR titles are fetched via the GitHub API
                        so entries read the real PR title instead of the commit subject.
    GITHUB_REPOSITORY   e.g. "owner/repo". Defaults to "DibyajyotiBiswal57/programs".
                        Set automatically by GitHub Actions.

How the script decides what to add:
    1. It reads CHANGELOG.md and collects every PR number ([#NN]) and every bullet
       entry already present in the [Unreleased] section.
    2. It finds the most-recent git tag (e.g. "0.1") and queries all commits since
       that tag using `git log`.
    3. For merge commits it extracts the PR number from the subject line.  When
       GITHUB_TOKEN is available it fetches the real PR title from the GitHub API.
    4. For non-merge commits it uses the commit subject directly.
    5. Bot commits (github-actions[bot], Auto-update … [skip ci]) are skipped.
    6. Each new entry is assigned a Keep-a-Changelog category (Added, Changed,
       Deprecated, Removed, Fixed, Security, Automated) based on keywords found in
       the commit/PR title.
    7. Entries whose PR number or text already appears in [Unreleased] are skipped,
       making the script fully idempotent.
    8. Any new [#NN] PR references are appended to the reference-links section at
       the bottom of the file.
"""

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

DEFAULT_REPO = "DibyajyotiBiswal57/programs"

def validate_repo(repo: str) -> str:
    """
    Validate a GitHub repository identifier from the environment.

    Expected format: "owner/repo", where both segments are non-empty and consist only
    of allowed characters. If validation fails, fall back to DEFAULT_REPO.
    """
    # GitHub allows a fairly broad character set, but we keep this strict to avoid
    # path manipulation. Adjust if you legitimately need other characters.
    if not isinstance(repo, str):
        return DEFAULT_REPO
    pattern = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
    if pattern.match(repo):
        return repo
    return DEFAULT_REPO


REPO = validate_repo(os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPO))
TOKEN = os.environ.get("GITHUB_TOKEN", "")
CHANGELOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CHANGELOG.md")

# Ordered list of Keep-a-Changelog categories (includes repo-custom "Automated")
CATEGORIES = [
    "Added",
    "Changed",
    "Deprecated",
    "Removed",
    "Fixed",
    "Security",
    "Automated",
]

# Keyword → category mapping (checked against lower-cased title)
CATEGORY_KEYWORDS = {
    "Security": ["secur", "vulnerab", "cve", "xss", "injection", "overflow", "sanitiz"],
    "Fixed": ["fix", "bug", "patch", "correct", "repair", "resolv"],
    "Removed": ["remov", "delet", "drop"],
    "Deprecated": ["deprecat"],
    "Added": ["add", "new", "creat", "introduc", "implement", "feat"],
    "Automated": ["auto", " ci", "workflow", "action", "bot", "linter", "generat", "schedul"],
    "Changed": [
        "change",
        "update",
        "refactor",
        "renam",
        "move",
        "improv",
        "enhanc",
        "rewrit",
        "modif",
        "bump",
        "upgrad",
    ],
}


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------


def _run(*args, check=False):
    """Run a git (or any) command; return stripped stdout."""
    result = subprocess.run(
        list(args),
        capture_output=True,
        text=True,
        cwd=os.path.dirname(os.path.abspath(__file__)) or ".",
    )
    if check and result.returncode != 0:
        print(f"Command failed: {' '.join(args)}\n{result.stderr}", file=sys.stderr)
    return result.stdout.strip()


def ensure_full_history():
    """Unshallow the clone so we can see all tags and commits."""
    # Ignore errors – a full clone will simply return a non-zero code
    subprocess.run(
        ["git", "fetch", "--unshallow"],
        capture_output=True,
        cwd=os.path.dirname(os.path.abspath(__file__)) or ".",
    )
    # Also fetch tags
    subprocess.run(
        ["git", "fetch", "--tags"],
        capture_output=True,
        cwd=os.path.dirname(os.path.abspath(__file__)) or ".",
    )


def get_base_ref():
    """Return the most-recent tag, or the initial commit SHA if no tags exist."""
    tags = _run("git", "tag", "--sort=-creatordate")
    if tags:
        return tags.split("\n")[0]
    return _run("git", "rev-list", "--max-parents=0", "HEAD")


def get_commits_since(base_ref):
    """Return list of {sha, subject, email} for non-merge commits since *base_ref*."""
    log = _run(
        "git",
        "log",
        f"{base_ref}..HEAD",
        "--pretty=format:%H\t%s\t%ae",
        "--no-merges",
    )
    commits = []
    for line in log.splitlines():
        parts = line.split("\t", 2)
        if len(parts) >= 2:
            commits.append(
                {
                    "sha": parts[0],
                    "subject": parts[1],
                    "email": parts[2] if len(parts) > 2 else "",
                }
            )
    return commits


def get_merge_commits_since(base_ref):
    """Return list of {sha, subject} for merge commits since *base_ref*."""
    log = _run(
        "git",
        "log",
        f"{base_ref}..HEAD",
        "--pretty=format:%H\t%s",
        "--merges",
    )
    commits = []
    for line in log.splitlines():
        parts = line.split("\t", 1)
        if len(parts) == 2:
            commits.append({"sha": parts[0], "subject": parts[1]})
    return commits


# ---------------------------------------------------------------------------
# GitHub API
# ---------------------------------------------------------------------------


def fetch_pr_info(pr_number):
    """Fetch PR title and labels from GitHub API; returns None on any error."""
    if not TOKEN:
        return None
    url = f"https://api.github.com/repos/{REPO}/pulls/{pr_number}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {TOKEN}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "update-changelog-bot")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return {
                "title": data.get("title", ""),
                "labels": [lb["name"] for lb in data.get("labels", [])],
            }
    except (urllib.error.URLError, urllib.error.HTTPError, Exception):
        return None


# ---------------------------------------------------------------------------
# Categorisation
# ---------------------------------------------------------------------------


def categorize(text, pr_info=None):
    """Return the best Keep-a-Changelog category for *text*."""
    if pr_info:
        # Check labels first (highest confidence)
        for label in pr_info.get("labels", []):
            lower = label.lower()
            for cat, keywords in CATEGORY_KEYWORDS.items():
                if any(k in lower for k in keywords):
                    return cat
        # Use PR title
        text = pr_info.get("title", text)

    text_lower = text.lower()
    for cat in CATEGORIES:
        if any(k in text_lower for k in CATEGORY_KEYWORDS[cat]):
            return cat
    return "Changed"


# ---------------------------------------------------------------------------
# CHANGELOG parsing helpers
# ---------------------------------------------------------------------------


def read_changelog():
    with open(CHANGELOG_FILE, "r", encoding="utf-8") as fh:
        return fh.read()


def write_changelog(content):
    with open(CHANGELOG_FILE, "w", encoding="utf-8") as fh:
        fh.write(content)


def get_existing_pr_numbers(content):
    """Return set of int PR numbers already referenced anywhere in the file."""
    return {int(m) for m in re.findall(r"\[#(\d+)\]", content)}


def get_existing_unreleased_entries(content):
    """Return set of first-line strings for bullets already in [Unreleased].

    Only the first line of each multi-line bullet is collected; this is enough
    for duplicate detection.
    """
    m = re.search(
        r"## \[Unreleased\](.*?)(?=^## \[|\Z)", content, re.DOTALL | re.MULTILINE
    )
    if not m:
        return set()
    entries = set()
    for line in m.group(1).splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            entries.add(stripped[2:].strip())
    return entries


def get_existing_ref_link_numbers(content):
    """Return set of int PR numbers that already have a [#NN]: link at the bottom."""
    return {int(m) for m in re.findall(r"^\[#(\d+)\]:", content, re.MULTILINE)}


# ---------------------------------------------------------------------------
# Entry building
# ---------------------------------------------------------------------------

_BOT_PATTERNS = re.compile(
    r"(github-actions|dependabot|auto-update|auto-fix|auto-regenerat"
    r"|skip ci|\[skip ci\]|auto-apply|linter fix|merge branch)",
    re.IGNORECASE,
)


def _is_bot_commit(subject, email):
    return "github-actions" in email or bool(_BOT_PATTERNS.search(subject))


def extract_pr_number(subject):
    m = re.search(r"#(\d+)", subject)
    return int(m.group(1)) if m else None


def build_new_entries(commits, merge_commits):
    """Return dict {category: [{"text": str, "pr": int|None}, …]}."""
    entries_by_category = {cat: [] for cat in CATEGORIES}
    seen_prs = set()

    # --- Merge commits (likely PRs) ---
    for commit in merge_commits:
        subject = commit["subject"]
        pr_num = extract_pr_number(subject)
        if pr_num and pr_num in seen_prs:
            continue
        if pr_num:
            seen_prs.add(pr_num)

        if _is_bot_commit(subject, ""):
            continue

        pr_info = fetch_pr_info(pr_num) if pr_num else None

        if pr_info and pr_info.get("title"):
            title = pr_info["title"].strip()
        else:
            # Strip "Merge pull request #NN from owner/branch" and use what follows;
            # if nothing follows, derive a readable title from the branch slug.
            m = re.match(r"Merge pull request #\d+ from [^/]+/(\S+)\s*(.*)", subject)
            if m:
                after = m.group(2).strip()
                if after:
                    title = after
                else:
                    # Convert branch slug → title, removing common prefixes
                    slug = re.sub(r"^(copilot|claude|feature|fix|chore)/", "", m.group(1))
                    title = slug.replace("-", " ").replace("_", " ").capitalize()
            else:
                title = subject

        cat = categorize(subject, pr_info)
        text = f"{title} ([#{pr_num}])" if pr_num else title
        entries_by_category[cat].append({"text": text, "pr": pr_num})

    # --- Regular commits ---
    for commit in commits:
        subject = commit["subject"].strip()
        email = commit.get("email", "")
        if _is_bot_commit(subject, email):
            continue
        # Skip changelog-only commits
        if re.search(r"changelog", subject, re.IGNORECASE):
            continue
        cat = categorize(subject)
        entries_by_category[cat].append({"text": subject, "pr": None})

    return entries_by_category


# ---------------------------------------------------------------------------
# CHANGELOG updating
# ---------------------------------------------------------------------------


def _entry_core(text):
    """Strip trailing ([#NN]) reference so we can compare content only."""
    return re.sub(r"\s*\(\[#\d+\]\)\s*$", "", text).lower().strip()


def update_unreleased_section(content, new_entries, existing_entries, existing_prs):
    """Insert new entries into the [Unreleased] section of *content*.

    Uses line-level insertion so existing multi-line bullets are preserved
    verbatim – only new ``- text`` lines are appended to each subsection.
    """
    pattern = re.compile(
        r"(## \[Unreleased\])(.*?)(?=^## \[|\Z)", re.DOTALL | re.MULTILINE
    )
    match = pattern.search(content)
    if not match:
        return content

    section_body = match.group(2)
    lines = section_body.split("\n")

    # Map category name → (start_line_idx, end_line_idx) within *lines*
    # start_line_idx points to the "### Category" line itself
    subsection_start = {}
    subsection_end = {}
    current_cat = None
    for i, line in enumerate(lines):
        if line.startswith("### "):
            if current_cat is not None:
                subsection_end[current_cat] = i
            current_cat = line[4:].strip()
            subsection_start[current_cat] = i
    if current_cat is not None:
        subsection_end[current_cat] = len(lines)

    existing_cores = {_entry_core(e) for e in existing_entries}
    added_any = False

    for cat in CATEGORIES:
        items = new_entries.get(cat, [])
        new_bullets = []

        for item in items:
            text = item["text"]
            pr = item["pr"]

            # Skip if PR already referenced anywhere in changelog
            if pr and pr in existing_prs:
                continue

            # Skip if equivalent text already present
            core = _entry_core(text)
            if core in existing_cores:
                continue

            new_bullets.append(f"- {text}")
            existing_entries.add(text)
            existing_cores.add(core)
            if pr:
                existing_prs.add(pr)

        if not new_bullets:
            continue

        added_any = True
        n = len(new_bullets)

        if cat in subsection_start:
            # Find the insertion point: just before trailing blank lines of subsection
            end_idx = subsection_end[cat]
            insert_idx = end_idx
            while insert_idx > subsection_start[cat] + 1 and not lines[insert_idx - 1].strip():
                insert_idx -= 1

            lines[insert_idx:insert_idx] = new_bullets

            # Shift all subsequent subsection boundaries
            for other in list(subsection_start):
                if subsection_start[other] >= insert_idx:
                    subsection_start[other] += n
                if subsection_end[other] >= insert_idx:
                    subsection_end[other] += n
        else:
            # Add a brand-new subsection at the end of the [Unreleased] body
            # Insert before any trailing blank lines that precede the next "## " header
            insert_idx = len(lines)
            while insert_idx > 0 and not lines[insert_idx - 1].strip():
                insert_idx -= 1

            new_sub = ["", f"### {cat}"] + new_bullets + [""]
            lines[insert_idx:insert_idx] = new_sub
            subsection_start[cat] = insert_idx + 1
            subsection_end[cat] = insert_idx + 1 + n

    if not added_any:
        return content

    new_section_body = "\n".join(lines)
    return content[: match.start(2)] + new_section_body + content[match.end(2) :]


def update_reference_links(content, pr_numbers):
    """Append missing [#NN] reference links at the bottom of *content*."""
    existing = get_existing_ref_link_numbers(content)
    new_prs = sorted(pr_numbers - existing)
    if not new_prs:
        return content

    new_links = "\n".join(
        f"[#{n}]: https://github.com/{REPO}/pull/{n}" for n in new_prs
    )

    # Find position of the last [#NN]: line and insert after it
    last_match = None
    for m in re.finditer(r"^\[#\d+\]: https?://[^\n]+", content, re.MULTILINE):
        last_match = m
    if last_match:
        pos = last_match.end()
        content = content[:pos] + "\n" + new_links + content[pos:]
    else:
        content = content.rstrip("\n") + "\n" + new_links + "\n"

    return content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    if not os.path.exists(CHANGELOG_FILE):
        print(f"Error: {CHANGELOG_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    ensure_full_history()

    content = read_changelog()
    existing_entries = get_existing_unreleased_entries(content)
    existing_prs = get_existing_pr_numbers(content)

    base_ref = get_base_ref()
    print(f"Base ref: {base_ref}")

    commits = get_commits_since(base_ref)
    merge_commits = get_merge_commits_since(base_ref)
    print(
        f"Found {len(commits)} regular commit(s) and "
        f"{len(merge_commits)} merge commit(s) since {base_ref}"
    )

    if not commits and not merge_commits:
        print("No new commits found. CHANGELOG.md is up to date.")
        return

    new_entries = build_new_entries(commits, merge_commits)

    # Collect new PR numbers across all categories
    all_new_prs = {
        item["pr"]
        for items in new_entries.values()
        for item in items
        if item["pr"]
    }

    content = update_unreleased_section(content, new_entries, existing_entries, existing_prs)
    content = update_reference_links(content, all_new_prs)

    write_changelog(content)
    print("CHANGELOG.md updated successfully.")


if __name__ == "__main__":
    main()
