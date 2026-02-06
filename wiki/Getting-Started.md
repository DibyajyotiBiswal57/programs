# Getting Started

Welcome! This guide will help you get started with the Programming Solutions Universe repository.

## 📋 Prerequisites

Before you begin, ensure you have:

- A GitHub account (for contributing)
- Git installed on your computer
- A compiler/interpreter for your chosen language(s)
- A text editor or IDE

## 🚀 Quick Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DibyajyotiBiswal57/programs.git
cd programs
```

### 2. Explore the Structure

```
programs/
├── python/          # Python solutions
├── java/            # Java solutions
├── c/               # C solutions
├── cpp/             # C++ solutions
├── csharp/          # C# solutions
├── qbasic/          # QBasic solutions
├── go/              # Go solutions
├── haskell/         # Haskell solutions
├── perl/            # Perl solutions
├── elixir/          # Elixir solutions
├── asm/             # Assembly solutions
├── fortran/         # Fortran solutions
├── lua/             # Lua solutions
├── ruby/            # Ruby solutions
├── vb/              # Visual Basic solutions
├── pwsh/            # PowerShell solutions
├── batch/           # Batch scripts
├── questions.md     # All problem statements
├── status.md        # Completion status
└── index.html       # Interactive status page
```

### 3. View the Interactive Status Page

#### Option A: Open Locally
```bash
# macOS
open index.html

# Windows
start index.html

# Linux
xdg-open index.html
```

#### Option B: View Online
Visit: https://dibyajyotibiswal57.github.io/programs/

## 🎯 Finding Problems

### Method 1: Browse questions.md
The `questions.md` file contains all 89+ problems organized by difficulty:
- **Beginner (1-20)**: Basic I/O, arithmetic, simple conditionals
- **Intermediate (21-50)**: Loops, strings, patterns
- **Advanced (51-89)**: Algorithms, special numbers, complex logic

### Method 2: Use the Status Page
The interactive HTML page shows:
- Which problems are solved in which languages
- ✅ Complete implementations
- ❗️ Beta/WIP implementations
- ❌ Not yet implemented

### Method 3: Direct File Navigation
Files follow the naming convention: `0000_filename.ext`

Example:
- Problem #1 (Hello World):
  - `python/0001_hello_world.py`
  - `java/0001_hello_world.java`
  - `c/0001_hello_world.c`

## 💻 Running Programs

### Python
```bash
cd python
python 0001_hello_world.py
# or
python3 0001_hello_world.py
```

### Java
```bash
cd java
javac 0001_hello_world.java
java HelloWorld
```

### C
```bash
cd c
gcc 0001_hello_world.c -o hello
./hello
```

### C++
```bash
cd cpp
g++ 0001_hello_world.cpp -o hello
./hello
```

### Go
```bash
cd go
go run 0001_hello_world.go
```

### Python (Advanced)
```bash
# Run with input redirection
python program.py < input.txt

# Run with command line arguments
python program.py arg1 arg2
```

## 🔍 Understanding Problem Files

Each solution file typically contains:

1. **Problem Statement** (as a comment)
2. **Input/Output Examples**
3. **The Solution Code**
4. **Author/Date Information** (sometimes)

Example structure:
```python
"""
Problem #1: Print "Hello World"
Filename: 0001_hello_world.py

Description:
Print "Hello World" to the console.

Expected Output:
Hello World
"""

# Solution
print("Hello World")
```

## 📚 Learning Path

### For Beginners
1. Start with problems 1-20
2. Choose a language you're learning
3. Read the problem in `questions.md`
4. Try to solve it yourself first
5. Compare with the repository solution
6. Try the same problem in another language

### For Intermediate Users
1. Focus on problems 21-50
2. Implement missing solutions
3. Optimize existing solutions
4. Add solutions in new languages
5. Contribute back to the repository

### For Advanced Users
1. Tackle problems 51-89
2. Implement in multiple languages
3. Add new problem suggestions
4. Improve automation scripts
5. Help review pull requests

## 🛠️ Development Environment Setup

### Recommended Tools

#### Code Editors
- **VS Code**: Great multi-language support
- **PyCharm**: Best for Python
- **IntelliJ IDEA**: Best for Java
- **Visual Studio**: Best for C#
- **Vim/Emacs**: For terminal enthusiasts

#### Extensions (VS Code)
- Python extension
- Java Extension Pack
- C/C++ Extension
- Code Runner
- GitLens

### Setting Up Language Environments

#### Python
```bash
# Check version
python --version

# Install Python 3.x from python.org if needed
```

#### Java
```bash
# Check version
java --version
javac --version

# Install JDK 8 or higher if needed
```

#### C/C++
```bash
# Check GCC
gcc --version
g++ --version

# Install build tools if needed (varies by OS)
```

## 🎨 Using the Status Page Features

The interactive HTML page includes:

### Dark Mode
- Click the 🌙/☀️ button in the top right
- Preference saved in browser

### Search/Filter
- Use browser's search (Ctrl+F / Cmd+F)
- Filter by language or problem number

### Navigation
- Click language badges to jump to folders
- Use problem numbers to reference questions.md

## 🤝 Ready to Contribute?

Once you're comfortable navigating the repository:

1. Read the [Contributing Guide](Contributing)
2. Check the [Code Style Guidelines](Code-Style)
3. Look for issues labeled "good first issue"
4. Fork the repository and start coding!

## ❓ Need Help?

- **Questions?** Check the [FAQ](FAQ)
- **Issues?** See [Troubleshooting](Troubleshooting)
- **Bug?** [Report it](https://github.com/DibyajyotiBiswal57/programs/issues/new?template=bug_report.md)
- **Stuck?** [Ask for help](https://github.com/DibyajyotiBiswal57/programs/issues/new?template=question.md)

## 📖 Next Steps

- [Choose a Language Guide](Language-Guides)
- [View Problem Index](Problem-Index)
- [Learn About Project Structure](Project-Structure)
- [Understand Automation](Automation)

---

**Happy Coding!** 🚀

[← Back to Home](Home) | [Language Guides →](Language-Guides)
