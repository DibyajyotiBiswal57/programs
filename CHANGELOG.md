# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- _No changes yet._

### Changed
- _No changes yet._

### Fixed
- _No changes yet._

### Automated
- _No changes yet._

### Removed
- _No changes yet._

### Deprecated
- _No changes yet._

## [1.0.0] - 2026-03-14

### Added
- CHANGELOG.md for tracking project changes
- Comprehensive browser compatibility support: IE edge mode meta tag, mobile theming,
  noscript warning, and `@supports` CSS fallbacks for Grid and backdrop-filter ([#34])
- Vendor prefixes for cross-browser CSS (`-webkit-backdrop-filter`, `user-select`,
  placeholder styling) ([#34])
- Create changelog file ([#38])
- Git checkout  b feature/amazing solution ([#32])
- Add design elements from website ([#30])
- Add dark background animations ([#29])
- Add dark mode background animation ([#28])
- Add animated background ([#26])
- Add gradient background and improve responsiveness ([#22])
- Add search functionality ([#21])
- Create interactive status page ([#17])
- Add bluish tint to website ([#11])
- New files!!!
- Add comprehensive browser compatibility support
- Added new Python files
- Create 0071_pattern_reverse_desc.py
- git commit -m 'Add: Python solution for problem 0062'
- Add Virgin Galactic-inspired design elements: starfield, parallax, glassmorphism, enhanced animations
- Fix transition timing and add base box-shadow to question badges
- Implement dark background and enhanced animations for dark mode
- Fix gradient animation by adding background-position to body styles
- Address code review: refactor particle colors and page load
- Add sticky top bar with search and quality of life features
- Add cool animated background with floating shapes and particles
- Initial plan for adding cool animated background
- Add accessibility support for reduced motion preference
- Add glitch effect to website background
- Add beta version of divisibility check
- Implement dynamic splash screen with real file loading tracking and skip button
- Add test gradient page and update .gitignore
- Add bluish-green animated gradient background for both themes
- Add comprehensive documentation for collapsible questions feature
- Add real status data fetching and workflow integration
- Create collapsible questions with iframe tables functionality
- Add dynamic gradient background and improve mobile responsiveness
- Add search functionality to index.html
- Create 0002_sum_of_three.c
- Create Quick-Start.md
- Create Installation-Setup.md
- Add Troubleshooting document
- Add devcontainer configuration for development environment
- Create New-Questions.md
- Create Code-Style.md
- Add files via upload
- Simplify README: replace full lists with links, add star/follow requests
- Add comprehensive documentation and repository improvements
- Add comprehensive templates and wiki content
- Create eye-catching README with modern design
- Implement dark mode, badge tip, remove subtitle, and update splash screen
- Add animated initialization splash screen
- Add documentation and README links for HTML status page
- Update update_status.py with new content
- Create 0090_test.py
- Add update_status.py script and update GitHub Actions workflow
- Create status.md file with status information
- Create codeql.yml
- Address code review feedback - improve conditions and comments
- Add lint-and-fix GitHub Actions workflow
- Create super-linter.yml
- Create python-app.yml
- Add bluish tint to website color scheme
- Add automated CHANGELOG.md update script and GitHub Actions workflow ([#39])
- Add .github/copilot-instructions.md for Copilot coding agent onboarding ([#41])
- Add .github/copilot-instructions.md with repository-wide Copilot instructions
- Add stale.yml workflow for managing inactive issues and PRs
- Create label.yml
- Add GitHub Actions workflow for greetings

### Changed
- Refactored README: extracted embedded content to dedicated files, added engagement
  CTAs and community links ([#19])
- Rewrote dark mode toggle with smooth animations: 0.6s cubic-bezier transitions,
  icon rotation, ripple effect, 12-particle burst, and `prefers-reduced-motion`
  support ([#27])
- Renamed `CONTRIBUTING.md` to `Contribution.md`
- Updated `CODEOWNERS` to include new contributors
- Renamed `FUNDING.yml` to `_FUNDING.yml`
- Edit website background glitch ([#25])
- Update splash screen text ([#24])
- Enhance questions page ([#23])
- Update website improvements ([#18])
- Update status md generation ([#16])
- Initial plan
- Update questions.md
- Reorganize and renumber questions in questions.md
- Total of 99 questions
- Update CODE_OF_CONDUCT.md
- Update CONTRIBUTING.md with pull request process and legend
- Completion of Python till Q91
- All Python files complete
- Python: Q83-86 done
- Final polish: Enhanced glassmorphism, grid pattern, scroll progress, and back-to-top button
- Update README with badges and project details
- Update README.md
- Rewrite dark mode with smooth animations
- Update generate_html.py
- Update index.html
- Code optimization: remove dead code and redundant operations
- Remove markdown backticks from example displays
- Display complete question details with filenames and examples
- Make background more subtle and pleasing to the eyes
- Optimize scroll event handlers by combining into single listener
- Update 0028_divisibility_check.py
- Refactor image loading code to eliminate duplication
- Remove unused scriptsToTrack variable
- Remove demo file and fix resource tracking code based on review feedback
- Fix badge labels and improve error logging per code review
- Fix question parsing and improve status data path handling
- Update index.html timestamp after verification
- Initial plan for dynamic gradient background and mobile improvements
- Remove duplicate no results message
- Update README.md content
- Update README.md with support details
- Update GitHub Actions workflow for HTML updates
- Update Installation-Setup.md
- Change project license from MIT to GPL 2.0
- Update Home.md
- Rename CONTRIBUTING.md to Contribution.md
- Update CODEOWNERS
- Rename FUNDING.yml to _FUNDING.yml
- Remove temporary file
- Remove redundant CSS classes from boot splash screen
- Replace splash screen with Linux boot-style design
- Remove orphaned CSS rule from media query
- Updated update_status.py file content
- Updated update_status.py with the latest content.
- Fix regex patterns and f-string formatting in update_status.py
- Remove generate_readme.py (replaced by update_status.py)
- Update issue templates
- Update CONTRIBUTING.md
- Update contact email for vulnerability reporting
- Update SECURITY.md
- Fix lint-and-fix.yml workflow with all required improvements
- Update super-linter.yml
- Update python-app.yml

### Fixed
- Security: validated user-controlled arithmetic input in `java/0002_sum_of_three.java`
  to prevent overflow and infinite results ([#36])
- Fix dark mode issue ([#31])
- Alert autofix 25 ([#15])
- Alert autofix 30 ([#14])
- Fix lint and fix workflow ([#13])
- Potential fix for code scanning alert no. 7: User-controlled data in arithmetic expression
- Fix dark mode initialization and prevent theme flash
- Fix dark mode: question cards now turn dark/black
- Initial plan to fix dark mode question cards
- Fix accessibility comment to reflect all animations disabled
- Fix mobile viewport overflow and prevent horizontal scrolling
- Correct instruction for reporting a vulnerability
- Fix link formatting in README.md
- Potential fix for code scanning alert no. 25: User-controlled data in arithmetic expression
- Potential fix for code scanning alert no. 27: User-controlled data in arithmetic expression
- Potential fix for code scanning alert no. 4: User-controlled data in arithmetic expression
- Potential fix for code scanning alert no. 30: User-controlled data in arithmetic expression
- Fix job condition to handle pull_request events correctly
- Fix syntax error in even number check
- Potential fix for code scanning alert no. 45: Partial server-side request forgery
- Potential fix for code scanning alert no. 31: User-controlled data in arithmetic expression ([#43])
- Fix concurrent workflow push race condition causing non-fast-forward errors ([#37])
- Fix non-fast-forward push errors in GitHub Actions workflows

### Automated
- GitHub Actions now auto-applies linter fixes across all supported languages
- `index.html` is automatically regenerated from `questions.md` and `status.md` on
  every push, on a schedule, and via `workflow_dispatch`

### Removed
- Delete python/0025_voting_eligibility.py
- Delete java/0025_voting_eligibility.java
- Delete COLLAPSIBLE_QUESTIONS_README.md
- Delete COLLAPSIBLE_QUESTIONS.md
- Delete .github/workflows/codeql.yml
- Delete .github/workflows/python-app.yml
- Delete .github/workflows/super-linter.yml

### Deprecated
- Fix deprecated action versions and python command inconsistency in workflows



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

[Unreleased]: https://github.com/DibyajyotiBiswal57/programs/compare/v1...HEAD
[1.0.0]: https://github.com/DibyajyotiBiswal57/programs/releases/tag/v1
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
[#11]: https://github.com/DibyajyotiBiswal57/programs/pull/11
[#13]: https://github.com/DibyajyotiBiswal57/programs/pull/13
[#14]: https://github.com/DibyajyotiBiswal57/programs/pull/14
[#15]: https://github.com/DibyajyotiBiswal57/programs/pull/15
[#16]: https://github.com/DibyajyotiBiswal57/programs/pull/16
[#17]: https://github.com/DibyajyotiBiswal57/programs/pull/17
[#18]: https://github.com/DibyajyotiBiswal57/programs/pull/18
[#21]: https://github.com/DibyajyotiBiswal57/programs/pull/21
[#22]: https://github.com/DibyajyotiBiswal57/programs/pull/22
[#23]: https://github.com/DibyajyotiBiswal57/programs/pull/23
[#24]: https://github.com/DibyajyotiBiswal57/programs/pull/24
[#25]: https://github.com/DibyajyotiBiswal57/programs/pull/25
[#26]: https://github.com/DibyajyotiBiswal57/programs/pull/26
[#28]: https://github.com/DibyajyotiBiswal57/programs/pull/28
[#29]: https://github.com/DibyajyotiBiswal57/programs/pull/29
[#30]: https://github.com/DibyajyotiBiswal57/programs/pull/30
[#31]: https://github.com/DibyajyotiBiswal57/programs/pull/31
[#32]: https://github.com/DibyajyotiBiswal57/programs/pull/32
[#38]: https://github.com/DibyajyotiBiswal57/programs/pull/38
[#39]: https://github.com/DibyajyotiBiswal57/programs/pull/39
[#41]: https://github.com/DibyajyotiBiswal57/programs/pull/41
[#37]: https://github.com/DibyajyotiBiswal57/programs/pull/37
[#43]: https://github.com/DibyajyotiBiswal57/programs/pull/43
