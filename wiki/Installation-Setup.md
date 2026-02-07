# Installation & Setup Guide

Welcome to the Installation & Setup guide for the Programming Solutions Universe! This guide will help you set up your development environment for working with the solutions in this repository.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Git** (version 2.0 or higher)
- **Text Editor or IDE** (VS Code, IntelliJ IDEA, PyCharm, etc.)
- **Internet connection** for downloading dependencies

## 🚀 Basic Setup

### 1. Clone the Repository

```bash
# Clone using HTTPS
git clone https://github.com/DibyajyotiBiswal57/programs.git

# OR clone using SSH
git clone git@github.com:DibyajyotiBiswal57/programs.git

# Navigate to the repository
cd programs
```

### 2. Explore the Structure

```bash
# View the repository structure
ls -la

# Key directories:
# - c/              C programming solutions
# - cpp/            C++ solutions
# - python/         Python solutions
# - java/           Java solutions
# - wiki/           Wiki documentation
# - questions.md    Problem index
```

## 🛠️ Language-Specific Setup

Choose the languages you want to work with and follow the corresponding setup instructions:

### Python Setup

**Requirements**: Python 3.7 or higher

```bash
# Check Python version
python --version
# or
python3 --version

# Install Python from https://www.python.org/downloads/ if not installed
```

**Optional: Create Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies (if any)
pip install -r requirements.txt  # if requirements.txt exists
```

### Java Setup

**Requirements**: JDK 8 or higher

```bash
# Check Java version
java -version
javac -version

# Install JDK from:
# - Oracle JDK: https://www.oracle.com/java/technologies/downloads/
# - OpenJDK: https://openjdk.org/
```

**Set JAVA_HOME (if not already set)**
```bash
# On Windows (PowerShell):
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"

# On macOS/Linux:
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
```

### C/C++ Setup

**Requirements**: GCC/G++ compiler or alternative

#### Windows
```bash
# Option 1: Install MinGW
# Download from: https://www.mingw-w64.org/

# Option 2: Install Visual Studio with C++ tools
# Download from: https://visualstudio.microsoft.com/

# Verify installation
gcc --version
g++ --version
```

#### macOS
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Verify installation
gcc --version
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install build-essential

# Fedora
sudo dnf install gcc gcc-c++

# Verify installation
gcc --version
g++ --version
```

### C# Setup

**Requirements**: .NET SDK

```bash
# Download from: https://dotnet.microsoft.com/download

# Verify installation
dotnet --version
```

### Ruby Setup

**Requirements**: Ruby 2.7 or higher

```bash
# Check Ruby version
ruby --version

# Install from: https://www.ruby-lang.org/en/downloads/

# Install bundler (if needed)
gem install bundler
```

### Go Setup

**Requirements**: Go 1.16 or higher

```bash
# Download from: https://golang.org/dl/

# Verify installation
go version

# Set up workspace (if needed)
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

### Perl Setup

**Requirements**: Perl 5.30 or higher

```bash
# Check Perl version
perl --version

# Most Unix-like systems have Perl pre-installed
# Windows: Install Strawberry Perl from https://strawberryperl.com/
```

### PowerShell Setup

**Requirements**: PowerShell 7.0 or higher (for cross-platform)

```bash
# Check PowerShell version
pwsh --version

# Download from: https://github.com/PowerShell/PowerShell
```

### Haskell Setup

**Requirements**: GHC and Cabal/Stack

```bash
# Install GHCup (recommended)
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh

# Verify installation
ghc --version
cabal --version
```

### Lua Setup

**Requirements**: Lua 5.4 or higher

```bash
# Check Lua version
lua -v

# Install from: https://www.lua.org/download.html

# Ubuntu/Debian
sudo apt install lua5.4

# macOS
brew install lua
```

### Elixir Setup

**Requirements**: Elixir 1.12 or higher, Erlang

```bash
# Install from: https://elixir-lang.org/install.html

# Verify installation
elixir --version
```

### QBasic/Visual Basic Setup

**QBasic**:
- Use DOSBox: https://www.dosbox.com/
- Download QBasic: Available in MS-DOS package

**Visual Basic**:
- Use Visual Studio Community Edition
- Download from: https://visualstudio.microsoft.com/

### Fortran Setup

**Requirements**: GFortran compiler

```bash
# Ubuntu/Debian
sudo apt install gfortran

# macOS
brew install gcc

# Verify installation
gfortran --version
```

### Assembly Setup

**Requirements**: NASM or MASM

```bash
# Install NASM
# Ubuntu/Debian
sudo apt install nasm

# macOS
brew install nasm

# Verify installation
nasm -version
```

### Batch Scripts

**Requirements**: Windows Command Prompt

- No installation needed on Windows
- Pre-installed with Windows OS

## 🔧 Development Tools Setup

### Recommended IDEs/Editors

#### Visual Studio Code (Recommended)
```bash
# Download from: https://code.visualstudio.com/

# Recommended Extensions:
# - Python (ms-python.python)
# - Java Extension Pack (vscjava.vscode-java-pack)
# - C/C++ (ms-vscode.cpptools)
# - Code Runner (formulahendry.code-runner)
# - GitLens (eamodio.gitlens)
```

#### JetBrains IDEs
- **PyCharm**: Python development
- **IntelliJ IDEA**: Java development
- **CLion**: C/C++ development
- **Rider**: C# development

Download from: https://www.jetbrains.com/

#### Other Options
- **Sublime Text**: https://www.sublimetext.com/
- **Atom**: https://atom.io/
- **Vim/Neovim**: For terminal-based editing

### Git Configuration

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default editor
git config --global core.editor "code --wait"  # VS Code
# or
git config --global core.editor "vim"

# Enable color output
git config --global color.ui auto
```

## 🧪 Testing Your Setup

### 1. Run a Simple Program

**Python Example:**
```bash
cd python
python hello_world.py
```

**Java Example:**
```bash
cd java
javac HelloWorld.java
java HelloWorld
```

**C Example:**
```bash
cd c
gcc hello_world.c -o hello_world
./hello_world  # Linux/macOS
hello_world.exe  # Windows
```

### 2. Verify Automation Scripts

```bash
# Check Python scripts
python generate_html.py
python update_status.py
```

## 🐛 Troubleshooting

### Common Issues

#### "Command not found" errors
- **Solution**: Ensure the programming language is installed and added to your system PATH

#### Permission denied errors (Linux/macOS)
```bash
# Make script executable
chmod +x script_name.sh
```

#### Port already in use
```bash
# Find and kill process using port (example: 8080)
# Linux/macOS:
lsof -ti:8080 | xargs kill -9

# Windows:
netstat -ano | findstr :8080
taskkill /PID <PID> /F
```

#### Git clone fails
- **Solution**: Check your internet connection
- **Solution**: Try HTTPS instead of SSH (or vice versa)
- **Solution**: Verify repository access permissions

### Need More Help?

- Check the [Troubleshooting Guide](Troubleshooting)
- Review [FAQ](FAQ)
- Open an [issue](https://github.com/DibyajyotiBiswal57/programs/issues)

## ✅ Next Steps

Now that you have everything set up:

1. 📖 Follow the [Quick Start Tutorial](Quick-Start) to run your first program
2. 🔍 Browse the [Problem Index](https://raw.githubusercontent.com/DibyajyotiBiswal57/programs/refs/heads/main/questions.md)
3. 💻 Pick a problem and start coding!
4. 🤝 Read the [Contributing Guide](Contributing) to contribute back

## 📚 Additional Resources

- [GitHub Documentation](https://docs.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [VS Code Documentation](https://code.visualstudio.com/docs)
- [Language-Specific Guides](Language-Guides)

---

**Last Updated**: 2026-02-07  
**Maintainer**: DibyajyotiBiswal57

💡 **Tip**: Bookmark this page for quick reference during setup!
```
