# 💻 Code Standards
- **Comments:** Include a brief comment at the top explaining what the program does.
- **Naming:** Use meaningful variable names within your code.
- **Formatting:** Ensure your code is properly indented (4 spaces for Java/Python/C#).
# Code Style Guidelines

Consistent code style makes it easier to read, review, and maintain solutions across many languages.

These are general guidelines; when in doubt, prefer existing patterns in the repository.

---

## 1. General Principles

- **Clarity over cleverness** – prioritize readability.
- **One problem, one solution file** per language (unless documented otherwise).
- Keep input/output strictly aligned with the problem statement.
- Add brief comments where logic is non‑obvious.

---

## 2. Language‑Specific Style

Use idiomatic style for each language:

- **Python:** Follow PEP 8 conventions (snake_case for functions/variables, etc.).
- **Java:** CamelCase for classes, camelCase for methods and variables.
- **C / C++:** Consistent indentation, meaningful names, and clear separation of logic into functions.

If the repository has linters/formatters configured (e.g., `.editorconfig`, `pyproject.toml`, etc.), follow their rules.

---

## 3. File & Naming Conventions

Use descriptive filenames, given in the [Problem Index](/questions.md).

---

## 4. Comments & Documentation

- At minimum, include a top‑level comment or docstring summarizing your approach.
- Document any assumptions or edge cases handled in your solution.
- Keep comments up‑to‑date with code changes.

---

## 5. Testing & Validation

- Test with example inputs from the problem statement.
- Add tests where the repository provides a testing framework or harness.
- Avoid committing debugging logs or print statements.

---

## 6. Automated Checks

The repository includes automated workflows (see [GitHub Actions](GitHub-Actions.md)) which may:

- Run linters or formatters
- Execute test suites
- Update the HTML status page

Make sure your code passes these checks before requesting a review.

---

[← Back to Home](Home.md) | [Adding a new problem →](Adding-New-Problem.md)

Last updated: 2026-03-02 11:10:33 UTC
