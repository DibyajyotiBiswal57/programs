import os

languages = ["qbasic", "java", "python", "c", "cpp", "csharp", "haskell", "perl", "go", "rust"]
num_problems = 150

status = {lang: {} for lang in languages}

for lang in languages:
    path = f"./{lang}"
    if os.path.exists(path):
        for file in os.listdir(path):
            try:
                num = int(file.split("_")[0])  # extract number
                fname = file.lower()

                # --- Auto-rename to 4-digit format ---
                new_name = f"{num:04d}_" + "_".join(file.split("_")[1:])
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
            except:
                pass

# --- Build table header and divider ---
header = "| #    | " + " | ".join(languages) + " |"
divider = "|------" + "".join([ "|:------:" for _ in languages ]) + "|"

lines = [header, divider]
for i in range(1, num_problems + 1):
    row = f"| {i:04d} "
    for lang in languages:
        row += f"| {status[lang].get(i, '❌')} "
    row += "|"
    lines.append(row)

table = "\n".join(lines)

legend = """
**Legend**  
- ✅ Finished  
- ❗️ Beta (released)  
- ❌ Unfinished  
"""

# Replace section in README.md between markers
with open("README.md", "r") as f:
    content = f.read()

start_marker = "<!-- STATUS_TABLE_START -->"
end_marker = "<!-- STATUS_TABLE_END -->"

new_table = f"{start_marker}\n\n# 📘 Program Status Table\n\n{table}\n\n{legend}\n{end_marker}"

if start_marker in content and end_marker in content:
    updated = content.split(start_marker)[0] + new_table + content.split(end_marker)[1]
else:
    updated = content + "\n\n" + new_table

with open("README.md", "w") as f:
    f.write(updated)
