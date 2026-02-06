# Wiki Content for GitHub Wiki

This directory contains the markdown files for the GitHub Wiki.

## Setup Instructions

To populate the GitHub Wiki with this content:

### Method 1: Manual Upload

1. Go to the repository's Wiki tab on GitHub
2. Create new pages matching the filenames here
3. Copy and paste the content from each file

### Method 2: Git Clone (Advanced)

```bash
# Clone the wiki repository
git clone https://github.com/DibyajyotiBiswal57/programs.wiki.git

# Copy wiki files
cp wiki/*.md programs.wiki/

# Commit and push
cd programs.wiki
git add .
git commit -m "Add comprehensive wiki documentation"
git push origin master
```

## Wiki Structure

```
wiki/
├── README.md (this file)
├── Home.md (Wiki home page)
├── Getting-Started.md (Setup and usage guide)
├── FAQ.md (Frequently asked questions)
├── Language-Guide-Python.md (Python-specific guide)
└── [More pages to be added]
```

## Wiki Pages Included

### Core Pages
- **Home.md**: Welcome page with navigation
- **Getting-Started.md**: Comprehensive setup and usage guide
- **FAQ.md**: Frequently asked questions and answers

### Language Guides
- **Language-Guide-Python.md**: Complete Python guide with examples

### Planned Pages
- Language-Guide-Java.md
- Language-Guide-C.md
- Language-Guide-Cpp.md
- Troubleshooting.md
- Project-Structure.md
- Contributing.md
- Automation.md
- Problem-Index.md
- Code-Style.md

## Creating Additional Pages

To add new wiki pages:

1. Create a new `.md` file in this directory
2. Follow the naming convention: `Page-Title.md` (with hyphens)
3. Add links to the page in `Home.md` navigation
4. Upload to GitHub Wiki

## Naming Convention

- Use hyphens to separate words: `Getting-Started.md`
- Use PascalCase for compound words: `Language-Guide-Python.md`
- Match the page title in the file

## Content Guidelines

- Use clear, concise language
- Include code examples where relevant
- Add navigation links at the bottom
- Keep consistent formatting
- Update Home.md navigation when adding new pages

## Links in Wiki

Internal wiki links use the format:
```markdown
[Link Text](Page-Name)
```

No need for `.md` extension in links.

## Updating the Wiki

Whenever you add or modify wiki content:

1. Update files in this `wiki/` directory
2. Commit to the main repository
3. Manually update the GitHub Wiki or use git clone method

## Note

The wiki is a separate git repository from the main code repository. Changes here don't automatically update the GitHub Wiki - they need to be manually synchronized.
