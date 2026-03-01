# Other Languages Guide

This page covers every language in the repository except C and C++. All solutions follow the canonical filenames in `questions.md` (four-digit prefix + slug) inside their language folder.

## Shared Conventions
- Keep the problem statement as a short header comment at the top of each solution file.
- Match existing indentation for the language (e.g., 4 spaces for Java, Python, C#, Ruby).
- Ensure programs read from standard input (when required) and print a trailing newline on output.
- Favor standard library solutions over external dependencies to keep setup simple.

## Run Commands by Language
- **Python**: `python3 python/0001_hello_world.py`
- **Java**: `javac java/0001_hello_world.java && java -cp java hello_world`
- **C#**: `csc /out:0001_hello_world.exe csharp/0001_hello_world.cs && ./0001_hello_world.exe`
- **Go**: `go run go/0001_hello_world.go`
- **Ruby**: `ruby ruby/0001_hello_world.rb`
- **Perl**: `perl perl/0001_hello_world.pl`
- **Lua**: `lua lua/0001_hello_world.lua`
- **Elixir**: `elixir elixir/0001_hello_world.exs`
- **Haskell**: `runghc haskell/0001_hello_world.hs` or `ghc haskell/0001_hello_world.hs -o 0001_hello_world`
- **Fortran**: `gfortran fortran/0001_hello_world.f90 -o 0001_hello_world && ./0001_hello_world`
- **PowerShell**: `pwsh pwsh/0001_hello_world.ps1`
- **Batch**: `cmd.exe /c batch\\0001_hello_world.bat` (on Windows environments)
- **Assembly**: assemble and link with your platform toolchain (e.g., `nasm` + `ld`) using the file in `asm/`.
- **QBASIC**: open the file from `qbasic/` in a compatible interpreter (e.g., QB64) and run it.
- **VB**: `vbc /out:0001_hello_world.exe vb/0001_hello_world.vb && ./0001_hello_world.exe`

## Contribution Checklist
- Filename and location match `questions.md` and the correct language folder.
- A brief top-of-file comment states the problem being solved.
- Output formatting (including newlines) matches examples in `questions.md`.
- Code runs with the standard toolchain for that language without extra dependencies.

[← Back to Language Guides](Language-Guides.md) 

Last updated: 2026-03-01 13:49:23 UTC
