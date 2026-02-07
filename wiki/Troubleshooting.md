# Troubleshooting

Common issues and their solutions when using the Programming Solutions Universe repository.

## Table of Contents

- [General Issues](#general-issues)
- [Python Issues](#python-issues)
- [Java Issues](#java-issues)
- [C/C++ Issues](#cc-issues)
- [Git Issues](#git-issues)
- [Status Page Issues](#status-page-issues)
- [Contribution Issues](#contribution-issues)

---

## General Issues

### Repository Won't Clone

**Problem**: `git clone` fails or times out

**Solutions**:
```bash
# Try HTTPS instead of SSH
git clone https://github.com/DibyajyotiBiswal57/programs.git

# Or SSH instead of HTTPS
git clone git@github.com:DibyajyotiBiswal57/programs.git

# Check your internet connection
ping github.com

# Clone with depth limit (faster)
git clone --depth 1 https://github.com/DibyajyotiBiswal57/programs.git
```

### Can't Find a Specific Program

**Problem**: Looking for a solution but can't locate the file

**Solutions**:
1. Check `questions.md` for the problem number
2. Use the naming convention: `0000_filename.ext`
3. Check the interactive `index.html` status page
4. The file may not exist yet (check for ❌ in status page)

```bash
# Search for files by name
find . -name "*palindrome*"

# Search for files by problem number
find . -name "0042_*"

# List all Python files
ls python/
```

### File Won't Open

**Problem**: File appears corrupted or won't open

**Solutions**:
- Ensure you're using the correct encoding (UTF-8)
- Try a different text editor
- Re-clone the repository
- Check if the file is actually a directory

```bash
# Check file type
file python/0001_hello_world.py

# Check file encoding
file -i python/0001_hello_world.py
```

---

## Python Issues

### "python: command not found"

**Problem**: Python isn't recognized

**Solutions**:

**Windows**:
```bash
# Try python3
python3 --version

# Or py launcher
py --version

# Add Python to PATH (reinstall with "Add to PATH" checked)
```

**macOS/Linux**:
```bash
# Use python3
python3 --version

# Create alias (add to ~/.bashrc or ~/.zshrc)
alias python=python3

# Install Python
# macOS
brew install python3

# Ubuntu/Debian
sudo apt-get install python3

# Fedora
sudo dnf install python3
```

### "No module named X"

**Problem**: Required module not found

**Solutions**:
```bash
# Install missing module
pip install module_name

# Or with pip3
pip3 install module_name

# Upgrade pip first
python -m pip install --upgrade pip

# Install from requirements.txt (if exists)
pip install -r requirements.txt
```

### SyntaxError: Unexpected Issues

**Problem**: Code runs on repository but not locally

**Solutions**:
- Check Python version (Python 2 vs Python 3)
- Ensure proper indentation (4 spaces)
- Check for tabs vs spaces
- Verify file encoding

```bash
# Check Python version
python --version

# Run with specific Python version
python3.9 script.py

# Check for mixed tabs/spaces
cat -A filename.py
```

### Unicode/Encoding Errors

**Problem**: Special characters cause errors

**Solutions**:
```python
# Add encoding declaration at top of file
# -*- coding: utf-8 -*-

# Or
#!/usr/bin/env python3
# coding: utf-8
```

```bash
# Run with UTF-8 encoding
PYTHONIOENCODING=utf-8 python script.py
```

---

## Java Issues

### "javac: command not found"

**Problem**: Java compiler not found

**Solutions**:
```bash
# Check if Java is installed
java -version

# Install JDK (not just JRE)
# Windows: Download from Oracle or use Chocolatey
choco install openjdk

# macOS
brew install openjdk

# Ubuntu/Debian
sudo apt-get install default-jdk

# Fedora
sudo dnf install java-latest-openjdk-devel

# Set JAVA_HOME
export JAVA_HOME=/path/to/java
export PATH=$JAVA_HOME/bin:$PATH
```

### "Could not find or load main class"

**Problem**: Java can't find the main class

**Solutions**:
```bash
# Ensure class name matches filename
# For file: HelloWorld.java
javac HelloWorld.java
java HelloWorld  # NOT java HelloWorld.class

# Check package declaration
# If file has: package com.example;
# Run: java com.example.HelloWorld

# Compile and run from correct directory
cd java
javac 0001_hello_world.java
java HelloWorld
```

### Public Class Name Mismatch

**Problem**: Class name doesn't match filename

**Solutions**:
- Use `class` instead of `public class` (as per repository guidelines)
- Or rename file to match class name
- Or rename class to match filename

```java
// Repository style (preferred)
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

### Version Incompatibility

**Problem**: Code uses features not in your Java version

**Solutions**:
```bash
# Check required Java version in comments
# Upgrade Java if needed

# Compile for specific version
javac --release 8 HelloWorld.java

# Check available Java versions
update-alternatives --list java  # Linux
/usr/libexec/java_home -V  # macOS
```

---

## C/C++ Issues

### "gcc: command not found"

**Problem**: C compiler not installed

**Solutions**:

**Windows**:
```bash
# Install MinGW
# Or use WSL (Windows Subsystem for Linux)

# Install via Chocolatey
choco install mingw

# Or install Visual Studio Build Tools
```

**macOS**:
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Or install via Homebrew
brew install gcc
```

**Linux**:
```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# Fedora
sudo dnf install gcc gcc-c++

# Arch
sudo pacman -S base-devel
```

### Compilation Errors

**Problem**: Code won't compile

**Solutions**:
```bash
# Enable warnings to see issues
gcc -Wall -Wextra program.c -o program

# Check for missing headers
# Ensure #include statements are correct

# Check for missing libraries
gcc program.c -o program -lm  # Link math library

# Use C99 or C11 standard
gcc -std=c99 program.c -o program
```

### Undefined Reference Errors

**Problem**: Linker can't find functions

**Solutions**:
```bash
# Link required libraries
gcc program.c -o program -lm  # Math library
gcc program.c -o program -lpthread  # Threading

# Ensure all source files are included
gcc file1.c file2.c -o program

# Check function declarations
# Ensure prototypes match implementations
```

### Segmentation Fault

**Problem**: Program crashes with segfault

**Solutions**:
- Check array bounds
- Verify pointer initialization
- Use debugger

```bash
# Compile with debug symbols
gcc -g program.c -o program

# Run with gdb
gdb ./program

# Run with valgrind (Linux)
valgrind ./program

# Check for:
# - Uninitialized pointers
# - Array out of bounds
# - Stack overflow
# - Use after free
```

---

## Git Issues

### Merge Conflicts

**Problem**: Can't merge or pull due to conflicts

**Solutions**:
```bash
# Update your fork
git fetch upstream
git merge upstream/main

# Resolve conflicts manually
# Edit conflicted files, remove conflict markers
# <<<<<<< HEAD
# your changes
# =======
# their changes
# >>>>>>> branch

# Mark as resolved
git add conflicted_file.ext
git commit -m "Resolve merge conflict"

# Or abort merge
git merge --abort
```

### Detached HEAD State

**Problem**: Git says "detached HEAD"

**Solutions**:
```bash
# Create a new branch from here
git checkout -b new-branch-name

# Or return to main branch
git checkout main

# Discard changes
git checkout main
```

### Push Rejected

**Problem**: `git push` fails

**Solutions**:
```bash
# Pull first
git pull origin main

# Or with rebase
git pull --rebase origin main

# Force push (use carefully!)
git push --force origin branch-name

# Check remote URL
git remote -v
```

### Fork Out of Sync

**Problem**: Your fork is behind the original repository

**Solutions**:
```bash
# Add upstream remote (once)
git remote add upstream https://github.com/DibyajyotiBiswal57/programs.git

# Fetch upstream changes
git fetch upstream

# Merge into your branch
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

---

## Status Page Issues

### Status Page Won't Load

**Problem**: `index.html` doesn't display correctly

**Solutions**:
- Check browser console for errors (F12)
- Ensure JavaScript is enabled
- Try a different browser
- Clear browser cache
- Use the online version: https://dibyajyotibiswal57.github.io/programs/

### Dark Mode Not Saving

**Problem**: Dark mode preference resets

**Solutions**:
- Check if cookies/localStorage are enabled
- Try a different browser
- Check browser privacy settings
- Clear site data and try again

### Status Not Updating

**Problem**: New solution doesn't show on status page

**Solutions**:
```bash
# Regenerate status manually
python3 update_status.py
python3 generate_html.py

# Check if files are named correctly
# Format: 0000_filename.ext

# Check if files are in correct folder
# python/, java/, c/, etc.

# Wait for GitHub Actions to run
# Check Actions tab on GitHub
```

---

## Contribution Issues

### PR Rejected - Naming Convention

**Problem**: Pull request rejected due to filename

**Solutions**:
- Follow naming convention: `0000_filename.ext`
- 4-digit problem number with leading zeros
- Use underscores, not spaces or hyphens
- Match the filename in `questions.md`

```bash
# Correct
0001_hello_world.py
0042_palindrome.java

# Incorrect
1_hello_world.py
42-palindrome.java
hello world.py
```

### PR Rejected - Wrong Folder

**Problem**: File in wrong language folder

**Solutions**:
```bash
# Check file extension matches folder
python/     # .py files
java/       # .java files
c/          # .c files
cpp/        # .cpp files

# Move file to correct location
git mv wrong_folder/file.py python/file.py
git commit -m "Move to correct folder"
```

### PR Rejected - Code Quality

**Problem**: Code doesn't meet standards

**Solutions**:
- Add descriptive comments
- Follow language style guide
- Use proper indentation (4 spaces)
- Test code before submitting
- Follow [Code Style Guidelines](Code-Style)

### Can't Push to Repository

**Problem**: Permission denied

**Solutions**:
- You can't push directly to the main repository
- You must fork it first
- Make changes in your fork
- Submit a pull request

```bash
# Correct workflow
1. Fork repository on GitHub
2. Clone YOUR fork
   git clone https://github.com/YOUR_USERNAME/programs.git
3. Make changes
4. Push to YOUR fork
   git push origin branch-name
5. Open Pull Request on GitHub
```

---

## Still Having Issues?

If you can't find a solution here:

1. **Search Existing Issues**: [GitHub Issues](https://github.com/DibyajyotiBiswal57/programs/issues)
2. **Check FAQ**: [FAQ Page](FAQ)
3. **Ask a Question**: [Open a new issue](https://github.com/DibyajyotiBiswal57/programs/issues/new?template=question.md)
4. **Email Support**: coder99957@dibyajyoti.is-a.dev

## Reporting Bugs

When reporting issues, include:
- Operating system and version
- Language/compiler version
- Error message (full text)
- Steps to reproduce
- What you expected vs what happened

---

[← Back to Home](Home) | [FAQ →](FAQ)