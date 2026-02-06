# 🛠️ Development Environment Setup

Complete guide for setting up your development environment.

## 📋 Prerequisites

### Required Tools
- Git (2.x or higher)
- GitHub Account
- Text Editor (VS Code recommended)

### Language Requirements
Install compilers/interpreters for your chosen language(s).

## 🚀 Quick Setup

### 1. Fork & Clone
```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR_USERNAME/programs.git
cd programs
```

### 2. Configure Git
```bash
git config user.name "Your Name"
git config user.email "your@email.com"
git remote add upstream https://github.com/DibyajyotiBiswal57/programs.git
```

### 3. Install Language Tools

#### Python
```bash
python3 --version  # Should be 3.6+
```

#### Java
```bash
java --version   # JDK 8+
javac --version
```

#### C/C++
```bash
gcc --version
g++ --version
```

## 🔧 VS Code Setup

### Recommended Extensions
- Python
- Java Extension Pack
- C/C++
- Code Runner
- GitLens

## 🌿 Git Workflow

```bash
# Create branch
git checkout -b feature/my-solution

# Make changes
git add .
git commit -m "Add: Description"

# Push
git push origin feature/my-solution
```

## 🧪 Testing

```bash
# Python
python3 solution.py

# Java
javac Solution.java && java Solution

# C/C++
gcc solution.c -o solution && ./solution
```

## ✅ Pre-PR Checklist

- [ ] Code tested and works
- [ ] Follows naming convention (`0000_filename.ext`)
- [ ] In correct language folder
- [ ] Commented appropriately

For detailed setup, see the [full documentation](README.md) or [Wiki](https://github.com/DibyajyotiBiswal57/programs/wiki).
