# Project Overview

The **Programming Solutions Universe** is a polyglot collection of programming challenges designed for learning, practice, and comparison across languages.

## Repository Structure

```
programs/
├── questions.md          # Authoritative list of all problems
├── status.md             # Completion status per problem/language
├── index.html            # Auto-generated interactive status page
├── <language>/           # One folder per language
│   └── 0000_filename.ext
├── wiki/                 # Wiki documentation source
├── src/                  # mdBook documentation source
└── .github/workflows/    # CI/CD automation
```

## Language Folders

| Folder | Language |
|--------|----------|
| `asm/` | Assembly |
| `batch/` | Batch |
| `c/` | C |
| `cpp/` | C++ |
| `csharp/` | C# |
| `elixir/` | Elixir |
| `fortran/` | Fortran |
| `go/` | Go |
| `haskell/` | Haskell |
| `java/` | Java |
| `lua/` | Lua |
| `perl/` | Perl |
| `pwsh/` | PowerShell |
| `python/` | Python |
| `qbasic/` | QBasic |
| `ruby/` | Ruby |
| `vb/` | Visual Basic |

## File Naming Convention

All solution files follow the format: `NNNN_problem_name.ext`

- `NNNN` — Four-digit zero-padded problem number
- `problem_name` — Snake-case description matching `questions.md`
- `.ext` — Language-specific extension

Example: `0001_hello_world.py`, `0001_hello_world.java`, `0001_hello_world.c`

## Automation

The repository uses several GitHub Actions workflows:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `update-html.yml` | Push to main | Regenerates `index.html` |
| `update-status.yml` | Push to main | Updates `status.md` |
| `lint-and-fix.yml` | Push/PR | Auto-formats code |
| `mdbook-deploy.yml` | Wiki/src changes | Builds and deploys this docs site |

## Interactive Status Page

The [status page](https://dibyajyotibiswal57.github.io/programs/) shows a live dashboard of which problems have been solved in each language, with dark/light mode and animated badges.

Last updated: 2026-03-25 14:36:57 UTC
