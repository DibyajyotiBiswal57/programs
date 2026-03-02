# Automation Scripts

This page explains the purpose of the automation scripts used in **Programming Solutions Universe**, especially those that support the HTML status page and repository maintenance.

> Script names and exact behavior may evolve; new scripts may be added; refer to script source files for authoritative details.

---

## 1. Overview

Automation scripts help:

- Analyze which problems have solutions in which languages
- Generate an **HTML status page**
- Update metadata and badges
- Integrate with CI/CD pipelines

Two key scripts are commonly referenced:

- `generate_html.py`
- `update_status.py`

---

## 2. `generate_html.py`

### Purpose

- Scans problem and solution directories
- Produces an HTML summary (status page) of which problems are solved in which languages
- May generate additional artifacts or reports (depending on implementation)

### Typical Usage

From the repository root:

```bash
python3 /generate_html.py
```

### Output

- An HTML file (or files) used as the **Interactive Status Page**.

---

## 3. `update_status.py`

### Purpose

- Updates internal metadata describing solution coverage
- May be used as a helper for `generate_html.py` or CI workflows

### Typical Usage

```bash
python3 scripts/update_status.py
```

Check script comments or `--help` output for exact usage.

---

## 4. Integration with GitHub Actions

These scripts are often called from workflows defined under `.github/workflows/`, for example:

- On push or pull request, to keep the status page current
- On a schedule, to refresh artifacts

Details are covered in [GitHub Actions](GitHub-Actions.md).

---

## 5. Modifying or Extending Scripts

If you add new languages or problem formats (see [Adding a New Language](Adding-New-Language.md) and [Adding a New Problem](Adding-New-Problem.md)), you may need to:

- Update script logic to detect new directories or file patterns
- Adjust how status is calculated or displayed
- Ensure changes remain backward‑compatible when possible

Always test locally before relying on CI.

---

## 6. Related Pages

- [Status Page](Status-Page.md)
- [GitHub Actions](GitHub-Actions.md)
- [Project Structure](Project-Structure.md)
- [Getting Started](Getting-Started.md)
