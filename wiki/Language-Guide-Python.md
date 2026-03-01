# Language Guide: Python

This guide covers conventions and tips for writing Python solutions in the Programming Solutions Universe repository.

## Environment setup
- Install Python 3.8+ (use your OS package manager or python.org).
- Optional: create a virtual environment to isolate dependencies.
- No additional packages are required for the existing challenge solutions.

## File naming and structure
- Filenames must match `questions.md` exactly (for example, `0007_factorial.py`).
- Place files in the `python/` directory.
- Add a brief header comment describing the problem at the top of each file.
- Use 4-space indentation and keep lines under 120 characters.

## Running solutions
Execute files directly with the interpreter:
```bash
python3 python/0001_hello_world.py
```
If the program requires input, pass it via standard input:
```bash
echo "5" | python3 python/0005_fibonacci.py
```

## Recommended practices
- Use functions to separate logic from input/output when helpful for clarity.
- Prefer built-in data structures and algorithms before adding external packages.
- Handle edge cases shown in `questions.md` examples (empty input, zero/negative values, large ranges).
- Keep solutions simple and readable; avoid premature optimization.

## Testing locally
- For pure functions, add quick assertions under a `if __name__ == "__main__":` guard to avoid interfering with problem I/O.
- When reading from `input()`, test with representative inputs using `echo` or heredocs.
- Remove any ad-hoc debug prints before committing.

## Troubleshooting
- **Unicode or locale errors**: stick to ASCII I/O unless the problem explicitly requires otherwise.
- **Time/space constraints**: use iterative approaches for recursion-heavy tasks when Python’s recursion depth may be a limit.
- **Formatting**: if available, run `python3 -m compileall python` to catch syntax errors; formatters (like `black`) may run in CI but are optional locally.
