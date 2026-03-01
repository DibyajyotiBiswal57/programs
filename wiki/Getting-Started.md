# Getting Started

This guide helps you set up the repository locally, run existing solutions, and add new ones with minimal effort.

## Prerequisites
- Git installed and access to clone the repository.
- Runtime or compiler for your target language (for example, Python 3, Go, Java, GCC/Clang).
- Optional: Python 3 if you plan to run helper scripts like `generate_html.py`.

## Clone the repository
```bash
git clone https://github.com/DibyajyotiBiswal57/programs.git
cd programs
```

## Explore problems
1. Open `questions.md` to choose a problem. The four-digit prefix is the canonical problem number.
2. Each solution filename must match the problem name exactly (for example, `0001_hello_world.py`).
3. Use `status.md` to see which languages already have solutions and which are open.

## Run a solution
Pick the language folder you want to use and run the file directly:
- Python: `python3 python/0001_hello_world.py`
- Go: `go run go/0001_hello_world.go`
- Java: `javac java/0001_hello_world.java && java hello_world`
- C: `gcc c/0001_hello_world.c -o /tmp/hello_world && /tmp/hello_world`

## Add a new solution
1. Copy the canonical filename from `questions.md`.
2. Create the file in the appropriate language folder using that exact filename.
3. Include a brief comment at the top describing the problem (follow existing style in that folder).
4. Keep indentation consistent with language norms (Python: 4 spaces; Java: formatted by google-java-format).
5. Test your program locally using your language runtime or compiler.

## Updating status
- Add new solutions to `status.md` following its existing table format.
- Do not edit `index.html`; it is generated automatically from `questions.md` and `status.md` via `generate_html.py`.
- GitHub Actions regenerate the live status page; you do not need to run it manually unless verifying locally.

## Contribution checklist
- [ ] Filename matches `questions.md`
- [ ] Problem comment included
- [ ] Program runs locally
- [ ] Status updated if a new solution is added
- [ ] Changes limited to the relevant files
