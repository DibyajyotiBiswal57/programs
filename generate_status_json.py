#!/usr/bin/env python3
"""
Generate status-data.json from the status information for use by questions-collapsible.js

This script scans language folders and generates a JSON file containing the status of each
program implementation across all languages.
"""

import os
import re
import json


# Language configuration matching update_status.py
LANGUAGE_CONFIG = {
    "qbasic": {"name": "QBasic", "ext": "bas"},
    "java": {"name": "Java", "ext": "java"},
    "python": {"name": "Python", "ext": "py"},
    "c": {"name": "C", "ext": "c"},
    "cpp": {"name": "C++", "ext": "cpp"},
    "csharp": {"name": "C#", "ext": "cs"},
    "haskell": {"name": "Haskell", "ext": "hs"},
    "perl": {"name": "Perl", "ext": "pl"},
    "go": {"name": "Go", "ext": "go"},
    "elixir": {"name": "Elixir", "ext": "exs"},
    "asm": {"name": "Assembly", "ext": "asm"},
    "fortran": {"name": "Fortran", "ext": "f90"},
    "lua": {"name": "Lua", "ext": "lua"},
    "ruby": {"name": "Ruby", "ext": "rb"},
    "vb": {"name": "Visual Basic", "ext": "vb"},
    "pwsh": {"name": "PowerShell", "ext": "ps1"},
    "batch": {"name": "Batch", "ext": "bat"},
}


def extract_question_number(filename):
    """
    Extract question number from a filename.
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


def scan_language_folders():
    """
    Scan all language folders and detect program status.
    
    Returns:
        Dictionary mapping question_number -> language -> {"status": status, "filename": filename}
    """
    # Structure: {question_num: {lang: {status, filename}}}
    status_data = {}

    for lang_folder, lang_info in LANGUAGE_CONFIG.items():
        if not os.path.exists(lang_folder):
            print(f"⚠️  Warning: Folder '{lang_folder}' not found. Skipping.")
            continue

        files = os.listdir(lang_folder)
        print(f"📁 Scanning {lang_folder}: found {len(files)} files")

        for file in files:
            filepath = os.path.join(lang_folder, file)

            # Skip directories
            if not os.path.isfile(filepath):
                continue

            # Extract question number
            num = extract_question_number(file)

            if num is not None:
                fname_lower = file.lower()

                # Initialize question number if not exists
                if num not in status_data:
                    status_data[num] = {}

                # Status detection logic (same as update_status.py)
                if "beta" in fname_lower or "wip" in fname_lower:
                    status = "beta"
                elif "unfinished" in fname_lower or "todo" in fname_lower:
                    status = "missing"
                else:
                    status = "done"

                status_data[num][lang_folder] = {
                    "status": status,
                    "filename": file,
                }

    return status_data


def generate_status_json():
    """
    Generate status-data.json file.
    """
    print("🚀 Starting status-data.json generation...")
    
    status_data = scan_language_folders()
    
    print(f"\n✅ Found status for {len(status_data)} questions")
    
    # Write to JSON file
    output_file = "assets/js/status-data.json"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(status_data, f, indent=2)
    
    print(f"✅ {output_file} successfully generated!")
    print(f"📊 Generated data for {len(status_data)} questions")


if __name__ == "__main__":
    generate_status_json()
