#!/usr/bin/env python3
"""
Generate README.md from questions.md and language folder scanning.

This script reads questions from questions.md, scans all language folders for programs,
detects their status, and generates a comprehensive README.md file with:
- Questions list section
- Status table (between markers)
- Programs links section

USAGE:
    python3 generate_readme.py

HOW IT WORKS:
    1. Reads all questions from questions.md (single source of truth)
    2. Scans all language folders (qbasic, java, python, c, cpp, etc.)
    3. Detects program status based on filename:
       - Files with "beta" or "wip" → ❗️ (Beta)
       - Files with "unfinished" or "todo" → ❌ (Unfinished)
       - All other files → ✅ (Finished)
    4. Generates complete README.md with questions and status table
    
WORKFLOW:
    To add or modify a question:
    1. Edit questions.md
    2. Run: python3 generate_readme.py
    3. Commit the updated files
    
    The script is idempotent - running it multiple times produces the same result.
"""

import os
import re
from pathlib import Path

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
    "rust": "Rust",
    "asm": "Assembly",
    "fortran": "Fortran",
    "lua": "Lua",
    "ruby": "Ruby",
    "vb": "Visual Basic",
    "pwsh": "PowerShell",
    "batch": "Batch"
}

# Maximum number of questions to track in status table
MAX_QUESTIONS = 150

# Status markers
STATUS_START_MARKER = "<!-- STATUS_TABLE_START -->"
STATUS_END_MARKER = "<!-- STATUS_TABLE_END -->"


def read_questions(questions_file="questions.md"):
    """
    Read questions from questions.md file.
    
    Args:
        questions_file: Path to the questions markdown file
        
    Returns:
        String containing all questions with preserved formatting
    """
    if not os.path.exists(questions_file):
        print(f"⚠️  Warning: {questions_file} not found. Using empty questions section.")
        return ""
    
    try:
        with open(questions_file, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"✅ Successfully read {len(content)} characters from {questions_file}")
        return content
    except Exception as e:
        print(f"❌ Error reading {questions_file}: {e}")
        return ""


def scan_language_folders():
    """
    Scan all language folders and detect program status.
    
    Returns:
        Dictionary mapping language -> question_number -> status_emoji
    """
    status = {lang: {} for lang in LANGUAGE_CONFIG.keys()}
    
    for lang in LANGUAGE_CONFIG.keys():
        if not os.path.exists(lang):
            print(f"⚠️  Warning: Folder '{lang}' not found. Skipping.")
            continue
            
        files = os.listdir(lang)
        print(f"📁 Scanning {lang}: found {len(files)} files")
        
        for file in files:
            # Extract question number from filename using regex
            # Looking for 3-4 digit numbers (e.g., 0001, 001, 0032, 1234)
            match = re.search(r'(\d{3,4})', file)
            if not match:
                # Try to extract from patterns like "1_hello_world"
                match = re.search(r'^(\d+)', file)
            
            if match:
                try:
                    num = int(match.group(1))
                    fname_lower = file.lower()
                    
                    # Status detection logic
                    if "beta" in fname_lower or "wip" in fname_lower:
                        status[lang][num] = "❗️"
                    elif "unfinished" in fname_lower or "todo" in fname_lower:
                        status[lang][num] = "❌"
                    else:
                        status[lang][num] = "✅"
                except ValueError:
                    pass
    
    return status


def generate_status_table(status):
    """
    Generate the status table in markdown format.
    
    Args:
        status: Dictionary mapping language -> question_number -> status_emoji
        
    Returns:
        String containing the formatted status table
    """
    folders = list(LANGUAGE_CONFIG.keys())
    
    # Create table header
    header = "| #    | " + " | ".join([LANGUAGE_CONFIG[l] for l in folders]) + " |"
    divider = "|:--- |" + "".join([" :---: |" for _ in folders])
    
    table_lines = [header, divider]
    
    # Generate rows for each question number
    for i in range(1, MAX_QUESTIONS + 1):
        row = f"| {i:04d} | " + " | ".join([status[l].get(i, "❌") for l in folders]) + " |"
        table_lines.append(row)
    
    return "\n".join(table_lines)


def generate_programs_links():
    """
    Generate the programs links section.
    
    Returns:
        String containing the programs links in HTML format
    """
    links = []
    for folder, display_name in LANGUAGE_CONFIG.items():
        links.append(f'<a href="/{folder}/"> [{display_name}] </a>')
    
    return "\nPrograms -\n" + "\n".join(links)


def generate_readme(questions_content, status_table):
    """
    Generate the complete README.md content.
    
    Args:
        questions_content: String containing all questions
        status_table: String containing the status table
        
    Returns:
        String containing the complete README.md
    """
    readme_parts = []
    
    # Header and questions section
    readme_parts.append("# List of all the topics I make programs on-")
    readme_parts.append("")
    readme_parts.append("> Note - This section is under construction. The question numbers and status do not match with the code.")
    readme_parts.append("")
    readme_parts.append(questions_content)
    readme_parts.append("")
    
    # Status table section with markers
    readme_parts.append(STATUS_START_MARKER)
    readme_parts.append("")
    readme_parts.append("# 📘 Status")
    readme_parts.append("")
    readme_parts.append(status_table)
    readme_parts.append("")
    readme_parts.append("**Legend** - ✅ Finished | ❗️ Beta | ❌ Unfinished")
    readme_parts.append("")
    readme_parts.append(STATUS_END_MARKER)
    readme_parts.append("")
    
    # Programs links section
    readme_parts.append(generate_programs_links())
    
    return "\n".join(readme_parts)


def main():
    """Main function to orchestrate README generation."""
    print("🚀 Starting README.md generation...")
    print("")
    
    # Step 1: Read questions from questions.md
    print("Step 1: Reading questions from questions.md")
    questions_content = read_questions("questions.md")
    print("")
    
    # Step 2: Scan language folders
    print("Step 2: Scanning language folders for programs")
    status = scan_language_folders()
    print("")
    
    # Step 3: Generate status table
    print("Step 3: Generating status table")
    status_table = generate_status_table(status)
    print("✅ Status table generated")
    print("")
    
    # Step 4: Generate complete README
    print("Step 4: Generating README.md")
    readme_content = generate_readme(questions_content, status_table)
    
    # Step 5: Write to file
    print("Step 5: Writing to README.md")
    try:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme_content)
            # Ensure file ends with a newline
            if not readme_content.endswith("\n"):
                f.write("\n")
        print("✅ README.md successfully generated!")
    except Exception as e:
        print(f"❌ Error writing README.md: {e}")
        return 1
    
    print("")
    print("🎉 Done! README.md has been updated.")
    return 0


if __name__ == "__main__":
    exit(main())
