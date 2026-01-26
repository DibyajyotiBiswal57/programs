import os

# --- CONFIGURATION ---
# Format: "folder_name": "Display Name"
language_config = {
    "qbasic": "QBasic",
    "java": "Java",
    "python": "Python",
    "c": "C",
    "cpp": "C++",
    "csharp": "C#",
    "haskell": "Haskell",
    "perl": "Perl",
    "go": "Go",
    "rust": "Rust"
}

# Extract folder names for the logic to process
folders = list(language_config.keys())
num_problems = 150

# Initialize status using folder names as keys
status = {lang: {} for lang in folders}

for lang in folders:
    path = f"./{lang}"
    if os.path.exists(path):
        for file in os.listdir(path):
            try:
                # Expecting format: 0001_filename.ext
                num = int(file.split("_")[0])  
                fname = file.lower()

                # --- Auto-rename to 4-digit format ---
                parts = file.split("_")
                new_name = f"{num:04d}_" + "_".join(parts[1:])
                if file != new_name:
                    os.rename(os.path.join(path, file), os.path.join(path, new_name))
                    file = new_name

                # --- Detect status ---
                if "beta" in fname:
                    status[lang][num] = "❗️"
                elif "unfinished" in fname:
                    status[lang][num] = "❌"
                else:
                    status[lang][num] = "✅"
            except Exception:
                pass

# --- Build table header using Display Names ---
header = "| #    | " + " | ".join([language_config[lang] for lang in folders]) + " |"
divider = "|------" + "".join([ "|:------:" for _ in folders ]) + "|"

lines = [header, divider]

# --- Build rows ---
for i in range(1, num_problems + 1):
    row = f"| {i:04d} "
    for lang in folders:
        # Use folder name 'lang' to fetch the status
        row += f"| {status[lang].get(i, '❌')} "
    row += "|"
    lines.append(row)

table = "\n".join(lines)

legend = """
**Legend** - ✅ Finished  
- ❗️ Beta (released)  
- ❌ Unfinished  
"""

# --- Update README.md ---
try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""

    new_table_content = f"{start_marker}\n\n# 📘 Status \n\n{table}\n\n{legend}\n{end_marker}"

    if start_marker in content and end_marker in content:
        # Replace existing section
        parts = content.split(start_marker)
        before = parts[0]
        after = parts[1].split(end_marker)[1]
        updated = before + new_table_content + after
    else:
        # Append to end if markers don't exist
        updated = content + "\n\n" + new_table_content

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)
    print("README.md updated successfully!")

except FileNotFoundError:
    print("Error: README.md not found.")
