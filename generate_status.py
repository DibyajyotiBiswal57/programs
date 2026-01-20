import os

languages = ["qbasic", "java", "python", "c", "cpp", "csharp", "haskell", "perl", "go", "rust"]
num_problems = 90

status = {lang: set() for lang in languages}

for lang in languages:
    path = f"./{lang}"
    if os.path.exists(path):
        for file in os.listdir(path):
            try:
                num = int(file.split("_")[0])  # assumes filenames like 01_sum.py
                status[lang].add(num)
            except:
                pass

header = "| # | " + " | ".join(languages) + " |"
divider = "|---:" + "|".join([":---:"] * len(languages)) + "|"

lines = [header, divider]
for i in range(1, num_problems + 1):
    row = f"| {i:02d} "
    for lang in languages:
        row += "| ✅ " if i in status[lang] else "| ❌ "
    row += "|"
    lines.append(row)

table = "\n".join(lines)

with open("STATUS.md", "w") as f:
    f.write("# 📘 Program Status Table\n\n")
    f.write(table)
