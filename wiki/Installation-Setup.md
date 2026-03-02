# 🛠️ Installation & Setup

This guide walks you through setting up a complete development environment for the Programming Solutions Universe repository.

## 📋 Prerequisites

Before you begin, make sure you have:
- **Git** installed ([git-scm.com](https://git-scm.com/downloads))
- **A GitHub account** (for contributing)
- **A text editor or IDE** (VS Code recommended)

---

## 1. Clone the Repository

```bash
git clone https://github.com/DibyajyotiBiswal57/programs.git
cd programs
```

---

## 2. Install Language Runtimes

Install only the languages you plan to use.

### 🐍 Python
```bash
# Check if already installed
python3 --version

# macOS (Homebrew)
brew install python3

# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Windows — download from https://python.org
```

### ☕ Java (JDK 17+)
```bash
# macOS (Homebrew)
brew install openjdk@17

# Ubuntu/Debian
sudo apt-get install openjdk-17-jdk

# Windows — download from https://adoptium.net
javac --version
```

### 🔵 C / C++
```bash
# macOS — install Xcode Command Line Tools
xcode-select --install

# Ubuntu/Debian
sudo apt-get install gcc g++ clang

# Windows — install MinGW-w64 or use WSL
gcc --version && g++ --version
```

### 💚 Go
```bash
# macOS
brew install go

# Ubuntu/Debian
sudo apt-get install golang-go

# Windows — download from https://go.dev/dl/
go version
```

### 💎 Ruby
```bash
# macOS
brew install ruby

# Ubuntu/Debian
sudo apt-get install ruby

ruby --version
```

### 🔷 C# (.NET SDK)
```bash
# All platforms — download from https://dotnet.microsoft.com/download
dotnet --version
```

### 🔵 Haskell (GHC + Cabal)
```bash
# Recommended: use GHCup
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
ghc --version
```

### 💜 Elixir
```bash
# macOS
brew install elixir

# Ubuntu/Debian
sudo apt-get install elixir

elixir --version
```

### 🟡 Lua
```bash
# macOS
brew install lua

# Ubuntu/Debian
sudo apt-get install lua5.4

lua -v
```

### 🟠 Perl
```bash
# macOS/Linux — usually pre-installed
perl --version

# Windows — download Strawberry Perl from https://strawberryperl.com
```

### 🔵 PowerShell
```bash
# macOS/Linux
brew install --cask powershell   # macOS
sudo apt-get install powershell  # Ubuntu

pwsh --version
```

### 🟫 QBasic / QB64
Download QB64-PE from https://qb64phoenix.com/ — cross-platform.

### 🟤 Fortran (gfortran)
```bash
# macOS
brew install gcc  # includes gfortran

# Ubuntu/Debian
sudo apt-get install gfortran

gfortran --version
```

### ⚫ Assembly (NASM)
```bash
# macOS
brew install nasm

# Ubuntu/Debian
sudo apt-get install nasm

nasm --version
```

### 🟦 Visual Basic (.NET)
Included with the .NET SDK — see the C# section above.

### 🪟 Batch Scripts
Batch (`.bat`) files run natively on Windows. On macOS/Linux, use Wine or WSL.

---

## 3. Verify Your Setup

After installing, verify everything runs:

```bash
python3 --version
java --version
gcc --version
go version
ruby --version
dotnet --version
```

---

## 4. Optional: Set Up a Virtual Environment (Python)

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

---

## 5. Editor Setup

### VS Code (Recommended)
Install the following extensions:
- **Python** (`ms-python.python`)
- **Extension Pack for Java** (`vscjava.vscode-java-pack`)
- **C/C++** (`ms-vscode.cpptools`)
- **Go** (`golang.go`)
- **Ruby** (`Shopify.ruby-lsp`)
- **Haskell** (`haskell.haskell`)

---

[← Back to Home](Home.md) | [Quick Start →](Quick-Start.md)

Last updated: 2026-03-02 UTC