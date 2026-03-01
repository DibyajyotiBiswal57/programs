# C++ Language Guide

Guidance for contributing and running C++ solutions in this repository.

## Prerequisites
- Install `g++` or `clang++` with C++17 support.
- Formatting is handled by the repo workflow with `clang-format`; keep 2-space indentation and modern C++ style.

## File Layout
- Store solutions in `cpp/` with the canonical filename from `questions.md` (e.g., `0001_hello_world.cpp`).
- Keep a single `main` per file and add a short header comment describing the program.
- Prefer the standard library over manual memory management when possible.

## Compile and Run
```bash
g++ -std=c++17 -Wall -Wextra -pedantic 0001_hello_world.cpp -o 0001_hello_world
./0001_hello_world
```
- Swap in `clang++` if desired. Use `-O2` for performance or `-fsanitize=address,undefined` for debugging.

## Implementation Tips
- Avoid `using namespace std;` in larger solutions; qualify symbols or import selectively.
- Use `std::vector`/`std::array` instead of raw arrays, and `std::string` for text.
- Prefer `const` correctness and pass large objects by reference.
- Ensure outputs end with a newline to satisfy expected results.

## Contribution Checklist
- Filename matches `questions.md` and resides in `cpp/`.
- Builds cleanly with `g++ -std=c++17 -Wall -Wextra -pedantic`.
- Formatting aligns with `clang-format` (2-space indents).
- Includes a brief top-of-file comment summarizing the solved problem.

[← Back to Language Guides](Language-Guides.md) | [Other Languages Guide →](Language-Guide-Other-Languages.md)
