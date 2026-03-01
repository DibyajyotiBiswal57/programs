# Home

Welcome to the Programming Solutions Universe wiki. This repository hosts 89+ programming challenges implemented across 17+ languages. Use this page as your launch pad to explore problems, track completion status, and find the right guide for your workflow.

## Quick navigation
- [[Getting-Started]] — set up your environment and run solutions locally.
- [[FAQ]] — common questions on naming, status, and contributions.
- [[Language-Guide-Python]] — tips for writing and testing Python solutions.
- [questions.md](../questions.md) — canonical list of problems and filenames.
- [status.md](../status.md) — current completion status by language.
- [Live status page](https://dibyajyotibiswal57.github.io/programs/) — interactive view generated from status data.

## Quick start
1. Clone the repo and switch into the project directory.
2. Open `questions.md` to choose a problem and note its canonical filename.
3. Pick a language folder, copy an existing solution as a template if needed, and keep the filename consistent with `questions.md`.
4. Run the program in your language runtime (examples are in [[Getting-Started]]).
5. Update `status.md` when adding new solutions and let automation regenerate `index.html`.

## What’s inside
- **Problems**: `questions.md` lists every challenge with problem numbers and filenames.
- **Solutions**: Language folders (`python/`, `java/`, `c/`, and more) store problem implementations.
- **Automation**: Scripts like `generate_html.py` and `update_status.py` keep the status site up to date.
- **Docs**: Additional guidance lives in `docs/` and this wiki.

## Contributing
- Follow the naming convention exactly (`0000_problem_name.ext` as defined in `questions.md`).
- Keep changes minimal and focused; avoid editing generated files such as `index.html`.
- Run existing formatters or linters available for your language when applicable.
- Open a pull request with a brief description of the problem solved and any testing performed.
