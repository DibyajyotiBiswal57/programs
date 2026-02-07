# Installation & Setup Guide

This guide will help you set up your development environment to run and contribute to the Programming Solutions Universe repository.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [General Setup](#general-setup)
- [Language-Specific Setup](#language-specific-setup)
- [Development Tools](#development-tools)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### Required
- **Git** (version 2.0 or higher)
- **Text Editor or IDE** (VS Code, IntelliJ IDEA, etc.)
- **Internet Connection** (for initial setup and package downloads)

### Optional
- **GitHub Account** (for contributing)
- **Docker** (for containerized development)

## General Setup

### 1. Clone the Repository

```bash
# Using HTTPS
git clone https://github.com/DibyajyotiBiswal57/programs.git

# Using SSH (recommended for contributors)
git clone git@github.com:DibyajyotiBiswal57/programs.git

# Navigate to the repository
cd programs
```

### 2. Explore the Structure

```bash
# View the directory structure
tree -L 2  # On Linux/Mac
# or
dir /s    # On Windows

# View available problems
cat questions.md
```

### 3. Choose Your Languages

Review the [Language Guides](Language-Guides) to determine which programming languages you want to work with, then proceed with the relevant language-specific setup below.

## Language-Specific Setup

### Python (3.7+)

#### Installation
```bash
# Check if Python is installed
python --version
# or
python3 --version

# Install Python from https://www.python.org/downloads/
# Or using package managers:

# macOS (Homebrew)
brew install python

# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Windows (Chocolatey)
choco install python
```

#### Verification
```bash
python3 --version
pip3 --version
```

#### Running Python Programs
```bash
cd python
python3 problem_001.py
```

### Java (JDK 11+)

#### Installation
```bash
# Check if Java is installed
java -version
javac -version

# Install OpenJDK:

# macOS (Homebrew)
brew install openjdk@11

# Ubuntu/Debian
sudo apt install openjdk-11-jdk

# Windows (Chocolatey)
choco install openjdk11
```

#### Verification
```bash
java -version
javac -version
```

#### Running Java Programs
```bash
cd java
javac Problem001.java
java Problem001
```

### C (GCC 7.0+)

#### Installation
```bash
# Check if GCC is installed
gcc --version

# Install GCC:

# macOS (Xcode Command Line Tools)
xcode-select --install

# Ubuntu/Debian
sudo apt install build-essential

# Windows (MinGW)
# Download from https://www.mingw-w64.org/
```

#### Verification
```bash
gcc --version
```

#### Running C Programs
```bash
cd c
gcc problem_001.c -o problem_001
./problem_001  # Linux/Mac
problem_001.exe  # Windows
```

### C++ (G++ 7.0+)

#### Installation
```bash
# Usually installed with GCC
g++ --version

# If not, follow C installation steps above
```

#### Running C++ Programs
```bash
cd cpp
g++ problem_001.cpp -o problem_001
./problem_001
```

### JavaScript (Node.js 14+)

#### Installation
```bash
# Download from https://nodejs.org/

# Or using package managers:

# macOS (Homebrew)
brew install node

# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

# Windows (Chocolatey)
choco install nodejs
```

#### Verification
```bash
node --version
npm --version
```

#### Running JavaScript Programs
```bash
cd javascript
node problem_001.js
```

### Ruby (2.7+)

#### Installation
```bash
# macOS (Homebrew)
brew install ruby

# Ubuntu/Debian
sudo apt install ruby-full

# Windows (RubyInstaller)
# Download from https://rubyinstaller.org/
```

#### Verification
```bash
ruby --version
```

#### Running Ruby Programs
```bash
cd ruby
ruby problem_001.rb
```

### Go (1.16+)

#### Installation
```bash
# Download from https://golang.org/dl/

# macOS (Homebrew)
brew install go

# Ubuntu/Debian
sudo apt install golang-go

# Windows (Chocolatey)
choco install golang
```

#### Verification
```bash
go version
```

#### Running Go Programs
```bash
cd go
go run problem_001.go
```

### Rust (1.50+)

#### Installation
```bash
# Install using rustup (recommended)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Windows: Download from https://rustup.rs/
```

#### Verification
```bash
rustc --version
cargo --version
```

#### Running Rust Programs
```bash
cd rust
rustc problem_001.rs
./problem_001
```

### C# (.NET 6.0+)

#### Installation
```bash
# Download from https://dotnet.microsoft.com/download

# macOS (Homebrew)
brew install --cask dotnet-sdk

# Ubuntu/Debian
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install dotnet-sdk-6.0
```

#### Verification
```bash
dotnet --version
```

#### Running C# Programs
```bash
cd csharp
dotnet run Problem001.cs
```

### Perl (5.30+)

#### Installation
```bash
# Usually pre-installed on Unix-like systems
perl --version

# macOS (Homebrew)
brew install perl

# Ubuntu/Debian
sudo apt install perl

# Windows (Strawberry Perl)
# Download from https://strawberryperl.com/
```

#### Running Perl Programs
```bash
cd perl
perl problem_001.pl
```

### PowerShell (7.0+)

#### Installation
```bash
# Download from https://github.com/PowerShell/PowerShell

# macOS (Homebrew)
brew install --cask powershell

# Ubuntu/Debian
sudo apt update
sudo apt install -y powershell

# Windows: Usually pre-installed
```

#### Verification
```bash
pwsh --version
```

#### Running PowerShell Scripts
```bash
cd powershell
pwsh problem_001.ps1
```

### Haskell (GHC 8.10+)

#### Installation
```bash
# Using GHCup (recommended)
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh

# macOS (Homebrew)
brew install ghc cabal-install

# Ubuntu/Debian
sudo apt install haskell-platform
```

#### Verification
```bash
ghc --version
```

#### Running Haskell Programs
```bash
cd haskell
ghc problem_001.hs
./problem_001
```

### Lua (5.3+)

#### Installation
```bash
# macOS (Homebrew)
brew install lua

# Ubuntu/Debian
sudo apt install lua5.3

# Windows (Chocolatey)
choco install lua
```

#### Verification
```bash
lua -v
```

#### Running Lua Programs
```bash
cd lua
lua problem_001.lua
```

## Development Tools

### Recommended IDEs and Editors

#### Visual Studio Code (Recommended)
```bash
# Download from https://code.visualstudio.com/

# Recommended extensions:
# - Python
# - Java Extension Pack
# - C/C++
# - Go
# - Rust
# - Code Runner (run code directly)
```

#### JetBrains IDEs
- **PyCharm** - Python
- **IntelliJ IDEA** - Java
- **CLion** - C/C++
- **GoLand** - Go
- **Rider** - C#

#### Other Options
- **Vim/Neovim** - For terminal enthusiasts
- **Sublime Text** - Lightweight and fast
- **Atom** - Hackable editor
- **Eclipse** - Java development

### Version Control

```bash
# Configure Git (if not already done)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Create a branch for your work
git checkout -b feature/your-feature-name
```

## Verification

### Test Your Setup

Run the verification script to test all installed languages:

```bash
# Make the script executable (Linux/Mac)
chmod +x scripts/verify_setup.sh

# Run verification
./scripts/verify_setup.sh
```

### Manual Verification

Test a simple program in your chosen language:

```bash
# Example: Test Python
cd python
python3 problem_001.py

# Example: Test Java
cd java
javac Problem001.java && java Problem001

# Example: Test C
cd c
gcc problem_001.c -o test && ./test
```

## Docker Setup (Optional)

For a containerized development environment:

```bash
# Install Docker
# Visit https://docs.docker.com/get-docker/

# Build the Docker image
docker build -t programs-universe .

# Run a container
docker run -it programs-universe

# Mount your local directory
docker run -it -v $(pwd):/workspace programs-universe
```

## Troubleshooting

### Command Not Found

If you get "command not found" errors:

1. **Check installation**: Verify the language is installed
2. **Update PATH**: Add the installation directory to your system PATH
3. **Restart terminal**: Close and reopen your terminal/command prompt
4. **Check aliases**: Some systems use `python3` instead of `python`

### Permission Denied

On Linux/Mac:
```bash
# Make scripts executable
chmod +x script_name.sh

# Or run with explicit interpreter
bash script_name.sh
```

### Package/Module Not Found

```bash
# Python
pip3 install package_name

# Node.js
npm install package_name

# Ruby
gem install package_name
```

### Windows-Specific Issues

- Run Command Prompt or PowerShell as Administrator
- Check Windows Defender/Antivirus isn't blocking executables
- Use forward slashes `/` or escaped backslashes `\\` in paths

### Still Having Issues?

- Check the [Troubleshooting](Troubleshooting) page
- Open an [issue](https://github.com/DibyajyotiBiswal57/programs/issues)
- Ask in [Discussions](https://github.com/DibyajyotiBiswal57/programs/discussions)

## Next Steps

✅ Setup complete! Now you can:

1. 📖 Follow the [Quick Start Tutorial](Quick-Start)
2. 🔍 Browse the [Problem Index](Problem-Index)
3. 💻 Check language-specific guides in [Language Guides](Language-Guides)
4. 🤝 Start [Contributing](Contributing)

---

**Need Help?** Contact: coder99957@dibyajyoti.is-a.dev

**Last Updated**: 2026-02-07
```
