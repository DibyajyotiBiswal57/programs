#!/usr/bin/env python3
"""
Generate status.md with Shields.io badges from questions.md and language folder scanning.

This script reads questions from questions.md, scans all language folders for programs,
detects their status, and generates a status.md file with Shields.io badges:
- Finished files: Green "done" badge with link to file
- Beta files (beta/wip): Yellow "beta" badge with link to file  
- Missing/unfinished files: Grey "missing" badge without link

USAGE:
    python3 update_status.py

HOW IT WORKS:
    1. Reads all questions from questions.md (single source of truth)
    2. Scans all language folders (qbasic, java, python, c, cpp, etc.)
    3. Detects program status based on filename:
       - Files with "beta" or "wip" → Beta (yellow badge)
       - Files with "unfinished" or "todo" → Missing (grey badge)
       - All other files → Finished (green badge)
    4. Generates status.md with Shields.io badge table

WORKFLOW:
    To add or modify a question:
    1. Edit questions.md
    2. Run: python3 update_status.py
    3. Commit the updated files

    The script is idempotent - running it multiple times produces the same result.
"""

import os
import re
from urllib.parse import quote

# --- CONFIGURATION ---
LANGUAGE_CONFIG = {
    "qbasic": "QBasic",
    "java": "Java",
    "python": "Python",
    "c": "C",
    "cpp": "C++",
    "csharp": "C#",
    "haskell": "Haskell",
    "perl": "Perl",
    "go": "Go",
    "elixir": "Elixir",
    "asm": "Assembly",
    "fortran": "Fortran",
    "lua": "Lua",
    "ruby": "Ruby",
    "vb": "Visual Basic",
    "pwsh": "PowerShell",
    "batch": "Batch",
}

def extract_question_number(filename):
    """
    Extract question number from a filename.

    Tries multiple filename patterns (0001, q1, 1_program, etc.)

    Args:
        filename: Name of the file

    Returns:
        Integer question number or None if not found
    """
    # Try 4-digit pattern first (0001, 0042, etc.)
    match = re.match(r"^(\d{4})", filename)
    if match:
        return int(match.group(1))

    # Try 3-digit pattern (001, 042, etc.)
    match = re.match(r"^(\d{3})", filename)
    if match:
        return int(match.group(1))

    # Try patterns like q1, q42, Q1, Q42
    match = re.match(r"^[qQ](\d+)", filename)
    if match:
        return int(match.group(1))

    # Try patterns like 1_program, 42_hello
    match = re.match(r"^(\d+)[_\-]", filename)
    if match:
        return int(match.group(1))

    # Try just a number at the start
    match = re.match(r"^(\d+)", filename)
    if match:
        return int(match.group(1))

    return None

def count_questions(questions_file="questions.md"):
    """
    Count the number of questions in questions.md.

    Args:
        questions_file: Path to the questions markdown file

    Returns:
        Integer representing the number of questions found
    """
    if not os.path.exists(questions_file):
        print(f"⚠️  Warning: {questions_file} not found. Using default count.")
        return 0

    try:
        with open(questions_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Count lines that start with a number followed by a period
        # Pattern: "1. ", "42. ", "123. ", etc."
        question_pattern = re.compile(r"^\d+\.\s+", re.MULTILINE)
        matches = question_pattern.findall(content)
        count = len(matches)

        print(f"📊 Found {count} questions in {questions_file}")
        return count
    except Exception as e:
        print(f"❌ Error counting questions in {questions_file}: {e}")
        return 0

def scan_language_folders():
    """
    Scan all language folders and detect program status.

    Returns:
        Dictionary mapping language -> question_number -> {"status": status, "filename": filename}
        where status is "done", "beta", or "missing"
    """
    status = {lang: {} for lang in LANGUAGE_CONFIG.keys()}

    for lang in LANGUAGE_CONFIG.keys():
        if not os.path.exists(lang):
            print(f"⚠️  Warning: Folder '{lang}' not found. Skipping.")
            continue

        files = os.listdir(lang)
        print(f"📁 Scanning {lang}: found {len(files)} files")

        for file in files:
            filepath = os.path.join(lang, file)

            # Skip directories
            if not os.path.isfile(filepath):
                continue

            # Extract question number using the new function
            num = extract_question_number(file)

            if num is not None:
                fname_lower = file.lower()

                # Status detection logic
                if "beta" in fname_lower or "wip" in fname_lower:
                    status[lang][num] = {"status": "beta", "filename": file}
                elif "unfinished" in fname_lower or "todo" in fname_lower:
                    status[lang][num] = {"status": "missing", "filename": file}
                else:
                    status[lang][num] = {"status": "done", "filename": file}

    return status

def create_shields_badge(status, label=None):
    """
    Create a Shields.io badge URL.

    Args:
        status: Status type ("done", "beta", or "missing")
        label: Optional custom label (defaults to status)

    Returns:
        Shields.io badge URL
    """
    # Badge configurations
    badge_config = {
        "done": {"label": "done", "color": "brightgreen"},
        "beta": {"label": "beta", "color": "yellow"},
        "missing": {"label": "missing", "color": "lightgrey"},
    }

    config = badge_config.get(status, badge_config["missing"])
    badge_label = quote(label or config["label"])
    badge_status = quote(config["label"])
    badge_color = config["color"]

    return f"https://img.shields.io/badge/{{badge_label}}-{{badge_status}}-{{badge_color}}"

def generate_status_table(status, num_questions):
    """
    Generate the status table in markdown format with Shields.io badges.

    Args:
        status: Dictionary mapping language -> question_number -> {"status": status, "filename": filename}
        num_questions: Number of questions to generate rows for

    Returns:
        String containing the formatted status table
    """
    folders = list(LANGUAGE_CONFIG.keys())

    # Create table header with clickable links to language directories
    header = (
        "| #    | "
        + " | ".join([f"[{LANGUAGE_CONFIG[l]}]({l}/)" for l in folders])
        + " |"
    )
    divider = "|:--- |" + "".join([" :---: |" for _ in folders])

    table_lines = [header, divider]

    # Generate rows for each question number (dynamic count)
    for i in range(1, num_questions + 1):
        cells = []
        for lang in folders:
            if i in status[lang]:
                status_info = status[lang][i]
                file_status = status_info["status"]
                filename = status_info["filename"]

                # Create Shields.io badge
                badge_url = create_shields_badge(file_status)

                # Create clickable link for done and beta, plain badge for missing
                if file_status in ["done", "beta"]:
                    file_path = f"{lang}/{filename}"
                    cells.append(f"[![{file_status}]({badge_url})]({file_path})")
                else:
                    # Missing/unfinished - plain badge without link
                    cells.append(f"![{file_status}]({badge_url})")
            else:
                # No file found - show plain missing badge
                badge_url = create_shields_badge("missing")
                cells.append(f"![missing]({badge_url})")

        row = f"| {i:04d} | " + " | ".join(cells) + " |"
        table_lines.append(row)

    return "\n".join(table_lines)

def generate_status_md(status_table):
    """
    Generate the complete status.md content.

    Args:
        status_table: String containing the status table

    Returns:
        String containing the complete status.md
    """
    status_parts = []

    # Header
    status_parts.append("# 📘 Status")
    status_parts.append("")
    status_parts.append("> [!TIP]")
    status_parts.append("> Click on the badges to view/download the code.")
    status_parts.append("")
    status_parts.append(status_table)
    status_parts.append("")

    # Legend section
    status_parts.append("## Legend")
    status_parts.append("")
    status_parts.append("| Badge | Status | Description |")
    status_parts.append("|:------|:-------|:------------|")

    # Create example badges for the legend
    done_badge = create_shields_badge("done")
    beta_badge = create_shields_badge("beta")
    missing_badge = create_shields_badge("missing")

    status_parts.append(
        f"| ![done]({done_badge}) | **Finished** | Program is complete and working |")
    status_parts.append(
        f"| ![beta]({beta_badge}) | **Beta** | Program is functional but may have issues or is work-in-progress |")
    status_parts.append(
        f"| ![missing]({missing_badge}) | **Missing** | Program not yet implemented or incomplete |")
    status_parts.append("")

    return "\n".join(status_parts)

def main():
    """Main function to orchestrate status.md generation."""
    print("🚀 Starting status.md generation...")
    print("")

    # Step 1: Count questions
    print("Step 1: Counting questions from questions.md")
    num_questions = count_questions("questions.md")
    if num_questions == 0:
        print("⚠️  Warning: No questions found. Using default of 150.")
        num_questions = 150
    print("")

    # Step 2: Scan language folders
    print("Step 2: Scanning language folders for programs")
    status = scan_language_folders()
    print("")

    # Step 3: Generate status table
    print("Step 3: Generating status table with Shields.io badges")
    status_table = generate_status_table(status, num_questions)
    print(f"✅ Status table generated with {num_questions} rows")
    print("")

    # Step 4: Generate complete status.md
    print("Step 4: Generating status.md")
    status_content = generate_status_md(status_table)

    # Step 5: Write to file
    print("Step 5: Writing to status.md")
    try:
        with open("status.md", "w", encoding="utf-8") as f:
            f.write(status_content)
            # Ensure file ends with a newline
            if not status_content.endswith("\n"):
                f.write("\n")
        print("✅ status.md successfully generated!")
    except Exception as e:
        print(f"❌ Error writing status.md: {e}")
        return 1

    print("")
    print("🎉 Done! status.md has been updated.")
    num_languages = len(LANGUAGE_CONFIG)
    print(f"📊 Generated table with {num_questions} questions across {num_languages} languages")
    return 0


if __name__ == "__main__":
    exit(main())
