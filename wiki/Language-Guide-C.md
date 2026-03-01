# C Language Guide

Guidance for writing and running C solutions in this repository.

## Prerequisites
- Install a C11-capable compiler (`gcc` or `clang`) and `make` if you prefer simple build scripts.
- The project formatting workflow runs `clang-format`; use 2-space indentation to match existing files.

## File Layout
- Place C solutions in `c/` using the exact canonical filename from `questions.md` (e.g., `0001_hello_world.c`).
- Keep one `main` function per file and a short header comment describing the program.
- Prefer standard library facilities; avoid platform-specific extensions.

## Compile and Run
```bash
# Compile with common warnings enabled
gcc -std=c11 -Wall -Wextra -pedantic 0001_hello_world.c -o 0001_hello_world
./0001_hello_world
```
- You can substitute `clang` for `gcc`. Add `-fsanitize=address` when debugging memory issues.

## Implementation Tips
- Always print a trailing newline on output to match expected results.
- Use `long long` for large integer calculations and `size_t` for indices/lengths.
- Initialize variables and check return values from `scanf` to avoid undefined behavior.
- For dynamic allocations, pair every `malloc/calloc` with `free`.

## Contribution Checklist
- Filename matches `questions.md` and lives in `c/`.
- Code compiles with `gcc -std=c11 -Wall -Wextra -pedantic`.
- Formatting aligns with repository style (`clang-format` friendly, 2-space indents).
- Include a brief top-of-file comment stating the problem the program solves.
