# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CHANGELOG.md for tracking project changes
- Comprehensive browser compatibility support: IE edge mode meta tag, mobile theming,
  noscript warning, and `@supports` CSS fallbacks for Grid and backdrop-filter ([#34])
- Vendor prefixes for cross-browser CSS (`-webkit-backdrop-filter`, `user-select`,
  placeholder styling) ([#34])

### Changed
- Refactored README: extracted embedded content to dedicated files, added engagement
  CTAs and community links ([#19])
- Rewrote dark mode toggle with smooth animations: 0.6s cubic-bezier transitions,
  icon rotation, ripple effect, 12-particle burst, and `prefers-reduced-motion`
  support ([#27])
- Renamed `CONTRIBUTING.md` to `Contribution.md`
- Updated `CODEOWNERS` to include new contributors
- Renamed `FUNDING.yml` to `_FUNDING.yml`

### Fixed
- Security: validated user-controlled arithmetic input in `java/0002_sum_of_three.java`
  to prevent overflow and infinite results ([#36])

### Automated
- GitHub Actions now auto-applies linter fixes across all supported languages
- `index.html` is automatically regenerated from `questions.md` and `status.md` on
  every push, on a schedule, and via `workflow_dispatch`

## [0.1] - 2026-01-29

> **Pre-release.** First tagged snapshot of the repository.

### Added
- Unified `questions.md` as the single source of truth for all programming questions,
  with a README generator script (`generate_readme.py`) ([#1])
- GitHub Actions workflow (`update-readme.yml`) with path filters and change detection
  to auto-update `README.md` ([#2])
- Dynamic status table sized to the actual question count ([#3])
- Improved README heading and legend formatting in `generate_readme.py` ([#4])
- Automatic file-renaming script to standardize 4-digit zero-padded filenames ([#6])
- Dark mode styling for the GitHub Pages site ([#7])
- Dark/light mode toggle button and collapsible status table ([#8])
- Modernized GitHub Pages site with sticky header, numbered questions, and premium
  design system ([#9])
- Clickable emoji links in the status table pointing directly to source files ([#10])

---

## Version History Notes

### Versioning Scheme
- **Major version**: Significant new features, breaking changes, or major refactoring
- **Minor version**: New problems, new languages, or feature additions
- **Patch version**: Bug fixes, documentation updates, or minor improvements

### Types of Changes
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` in case of vulnerabilities

---

[Unreleased]: https://github.com/DibyajyotiBiswal57/programs/compare/0.1...HEAD
[0.1]: https://github.com/DibyajyotiBiswal57/programs/releases/tag/0.1

[#1]: https://github.com/DibyajyotiBiswal57/programs/pull/1
[#2]: https://github.com/DibyajyotiBiswal57/programs/pull/2
[#3]: https://github.com/DibyajyotiBiswal57/programs/pull/3
[#4]: https://github.com/DibyajyotiBiswal57/programs/pull/4
[#6]: https://github.com/DibyajyotiBiswal57/programs/pull/6
[#7]: https://github.com/DibyajyotiBiswal57/programs/pull/7
[#8]: https://github.com/DibyajyotiBiswal57/programs/pull/8
[#9]: https://github.com/DibyajyotiBiswal57/programs/pull/9
[#10]: https://github.com/DibyajyotiBiswal57/programs/pull/10
[#19]: https://github.com/DibyajyotiBiswal57/programs/pull/19
[#27]: https://github.com/DibyajyotiBiswal57/programs/pull/27
[#34]: https://github.com/DibyajyotiBiswal57/programs/pull/34
[#36]: https://github.com/DibyajyotiBiswal57/programs/pull/36
