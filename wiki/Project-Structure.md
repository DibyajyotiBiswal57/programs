# Project Structure

This page describes the overall layout of the **Programming Solutions Universe** repository and how the pieces fit together.

> Note: Exact paths and filenames may differ slightly; refer to the repository for the most accurate view.

---

## 1. Top‑Level Layout (Conceptual)

Some typical top‑level entries you may see:

- `wiki/` – Documentation pages (this directory)  
- Configuration files for tools and CI  
- `LICENSE`, `README`, etc.

---

## 2. Problems

Problems are defined in a structured way so that they can be:

- Listed in the [Problem Index](/questions.md)
- Referenced consistently by ID or name
- Used by automation to build a status view

Check the [Problem Index](/questions.md) related files and [Adding a New Problem](Adding-New-Problem.md) for more details.

---

## 3. Solutions

Solutions are generally organized by language, for example:

- `python/`
- `java/`
- `c/`
- `cpp/`
- Additional directories for other supported languages

Each problem typically has:

- A separate file (or small group of files)
- Naming conventions aligned with the problem ID or title

See [Language Guides](Language-Guides.md) for language‑specific details.

---

## 4. Automation & Scripts

The scripts (usually found in the parent directory) are used to:

- Analyze the repository for solved/unsolved problems
- Generate the HTML **status page**
- Update metadata or badges

Key scripts include:

- `generate_html.py` – Generates HTML status pages
- `update_status.py` – Updates solution/coverage status

See [Automation Scripts](Automation.md) for how to use them.

---

## 5. Continuous Integration (CI)

Under `.github/workflows/`, you’ll find one or more workflow files that:

- Run tests and linters
- Regenerate and publish the status page
- Perform other checks on pull requests

These are described in more detail in [Automation](Automation.md).

---

## 6. Documentation

The `wiki/` directory (this one) contains:

- [Home](Home.md)
- [Getting Started](Getting-Started.md)
- [Installation & Setup](Installation-Setup.md)
- [Language Guides](Language-Guides.md) and language‑specific pages
- [Contributing‑related pages](Adding-New-Language.md, Adding-New-Problem.md, Code-Style.md)
- [FAQ](FAQ.md), [Troubleshooting](Troubleshooting.md)
- and more

---

[Back to Home](Home.md) | [Automation](Automation.md)

Last updated: 2026-03-02 11:37:34 UTC
