"""Append or refresh a last-updated timestamp at the bottom of Markdown files."""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List

TIMESTAMP_PREFIX = "Last updated: "


def current_timestamp() -> str:
    """Return a UTC timestamp string suitable for Markdown."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def apply_timestamp_to_content(content: str, timestamp: str) -> str:
    """Return content with a single timestamp line at the end."""
    stripped = content.rstrip("\n")
    lines = stripped.split("\n") if stripped else []
    if lines and lines[-1].startswith(TIMESTAMP_PREFIX):
        lines[-1] = f"{TIMESTAMP_PREFIX}{timestamp}"
    else:
        if lines:
            lines.append("")
        lines.append(f"{TIMESTAMP_PREFIX}{timestamp}")
    return "\n".join(lines) + "\n"


def update_file(path: Path, timestamp: str) -> bool:
    """Apply the timestamp to a file, returning True if the file changed."""
    if not path.is_file():
        print(f"Skipping missing file: {path}", file=sys.stderr)
        return False

    original = path.read_text(encoding="utf-8")
    updated = apply_timestamp_to_content(original, timestamp)
    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


def gather_markdown_files(repo_root: Path, provided_files: Iterable[str]) -> List[Path]:
    """Get Markdown files to update based on CLI input or git status."""
    if provided_files:
        paths: List[Path] = []
        for file_arg in provided_files:
            candidate = Path(file_arg)
            if candidate.suffix.lower() != ".md":
                continue

            if not candidate.is_absolute():
                candidate = (repo_root / candidate).resolve()

            if candidate.is_file():
                paths.append(candidate)
            else:
                print(f"Skipping missing file: {candidate}", file=sys.stderr)
        return paths

    try:
        result = subprocess.run(
            [
                "git",
                "ls-files",
                "--modified",
                "--others",
                "--exclude-standard",
                "--",
                "*.md",
            ],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_root,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"Unable to determine changed Markdown files: {exc}", file=sys.stderr)
        return []

    paths = []
    for line in result.stdout.splitlines():
        candidate = (repo_root / line.strip()).resolve()
        if candidate.is_file():
            paths.append(candidate)

    return paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Append a last-updated timestamp to Markdown files."
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Optional Markdown files to update; defaults to modified/untracked .md files detected by git.",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = Path(__file__).resolve().parent
    markdown_files = gather_markdown_files(repo_root, args.files)

    if not markdown_files:
        print("No Markdown files to update.")
        return 0

    timestamp = current_timestamp()
    updated_count = 0
    for file_path in markdown_files:
        if update_file(file_path, timestamp):
            updated_count += 1
            print(f"Updated {file_path.relative_to(repo_root)}")

    if updated_count == 0:
        print("Timestamps already current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
