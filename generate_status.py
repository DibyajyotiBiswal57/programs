import os

languages = ["qbasic", "java", "python", "c", "cpp", "csharp", "haskell", "perl", "go", "rust"]
num_problems = 90

status = {lang: {} for lang in languages}

for lang in languages:
    path = f"./{lang}"
    if os.path.exists(path):
        for file in os.listdir(path):
            try:
                num = int(file.split("_")[0])  # assumes filenames like 01_sum.py
                fname = file.lower()
                if "beta" in fname:
                    status[lang][num] = "❗️"
                elif "unfinished" in fname:
                    status[lang][num] = "❌"
                else:
                    status[lang][num] = "✅"
            except:
                pass

header = "| # | " + " | ".join(languages) + " |"
divider = "|---:" + "|".join([":---:"] * len(languages)) + "|"

lines = [header, divider]
for i in range(1, num_problems + 1):
    row = f"| {i:02d} "
    for lang in languages:
        row += f"| {status[lang].get(i, '❌')} "
    row += "|"
    lines.append(row)

table = "\n".join(lines)

# Replace section in README.md between markers
with open("README.md", "r") as f:
    content = f.read()

start_marker = "<!-- STATUS_TABLE_START -->"
end_marker = "<!-- STATUS_TABLE_END -->"

new_table = f"{start_marker}\n\n# 📘 Program Status Table\n\n{table}\n\n{end_marker}"

if start_marker in content and end_marker in content:
    updated = content.split(start_marker)[0] + new_table + content.split(end_marker)[1]
else:
    updated = content + "\n\n" + new_table

with open("README.md", "w") as f:
    f.write(updated)
