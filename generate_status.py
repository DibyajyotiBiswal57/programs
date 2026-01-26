import os

# --- CONFIGURATION ---
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
    "rust": "Rust",
    "asm": "Assembly",
    "fortran": "Fortran",
    "lua": "Lua",
    "ruby": "Ruby",
    "vb": "Visual Basic",
    "pwsh": "PowerShell",
    "batch": "Batch"
}

folders = list(language_config.keys())
num_problems = 150
status = {lang: {} for lang in folders}

# --- SCANNING FOLDERS ---
for lang in folders:
    if os.path.exists(lang):
        for file in os.listdir(lang):
            try:
                num = int(file.split("_")[0])
                fname = file.lower()
                
                # Logic for status icons
                if "beta" in fname:
                    status[lang][num] = "❗️"
                elif "unfinished" in fname:
                    status[lang][num] = "❌"
                else:
                    status[lang][num] = "✅"
            except:
                pass

# --- GENERATING THE TABLE STRING ---
header = "| #    | " + " | ".join([language_config[l] for l in folders]) + " |"
divider = "|:--- |" + "".join([ " :---: |" for _ in folders ])

table_lines = [header, divider]
for i in range(1, num_problems + 1):
    row = f"| {i:04d} | " + " | ".join([status[l].get(i, "❌") for l in folders]) + " |"
    table_lines.append(row)

full_table = "\n".join(table_lines)

# --- WRITING TO README.md ---
START = ""
END = ""

try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # The content we want to insert
    new_section = f"{START}\n\n# 📘 Status\n\n{full_table}\n\n**Legend** - ✅ Finished | ❗️ Beta | ❌ Unfinished\n\n{END}"

    if START in content and END in content:
        # Standard replacement
        before = content.split(START)[0]
        after = content.split(END)[1]
        final_content = before + new_section + after
        print("✅ Found markers. Replacing existing table.")
    else:
        # Force append if markers are missing
        final_content = content + "\n\n" + new_section
        print("⚠️ Markers not found. Appending table to the bottom of README.")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(final_content)
    
    print("🚀 README.md has been successfully overwritten!")

except Exception as e:
    print(f"❌ Error: {e}")
