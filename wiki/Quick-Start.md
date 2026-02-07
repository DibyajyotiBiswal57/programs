# Quick Start Tutorial

Welcome! This tutorial will guide you through running your first program from the Programming Solutions Universe repository. Let's get started! 🚀

## 🎯 What You'll Learn

By the end of this tutorial, you will:
- ✅ Navigate the repository structure
- ✅ Find and understand a problem
- ✅ Run a solution in your preferred language
- ✅ Modify and test the code
- ✅ View the interactive status page

**Estimated Time**: 15-20 minutes

## 📋 Prerequisites

Before starting, ensure you have:
- ✅ Cloned the repository (see [Installation & Setup](Installation-Setup))
- ✅ Installed at least one programming language
- ✅ A text editor or IDE ready

## 🗺️ Step 1: Explore the Repository

### Understanding the Structure

```
programs/
├── python/           # Python solutions
├── java/             # Java solutions
├── c/                # C solutions
├── cpp/              # C++ solutions
├── csharp/           # C# solutions
├── ruby/             # Ruby solutions
├── go/               # Go solutions
├── perl/             # Perl solutions
├── powershell/       # PowerShell solutions
├── haskell/          # Haskell solutions
├── lua/              # Lua solutions
├── elixir/           # Elixir solutions
├── qbasic/           # QBasic solutions
├── vb/               # Visual Basic solutions
├── fortran/          # Fortran solutions
├── batch/            # Batch scripts
├── assembly/         # Assembly solutions
├── questions.md      # Problem index
├── status.html       # Interactive status tracker
├── generate_html.py  # HTML generator script
└── update_status.py  # Status updater script
```

### Navigate to the Repository

```bash
cd programs
ls -la
```

## 📖 Step 2: Choose a Problem

### View Available Problems

```bash
# Open the problem index
cat questions.md

# OR view it on GitHub
# https://raw.githubusercontent.com/DibyajyotiBiswal57/programs/refs/heads/main/questions.md
```

### For This Tutorial

We'll use a simple problem: **"Print Hello World"**

**Problem Description**: Write a program that prints "Hello, World!" to the console.

**Difficulty**: Easy ⭐

## 💻 Step 3: Run Your First Program

Choose your preferred language and follow the corresponding section:

### Option A: Python 🐍

```bash
# Navigate to Python directory
cd python

# Check if hello_world.py exists
ls | grep hello

# Run the program
python hello_world.py

# Expected Output:
# Hello, World!
```

**View the Code:**
```python
# Typical hello_world.py content
print("Hello, World!")
```

### Option B: Java ☕

```bash
# Navigate to Java directory
cd java

# Find the HelloWorld file
ls | grep -i hello

# Compile the program
javac HelloWorld.java

# Run the program
java HelloWorld

# Expected Output:
# Hello, World!
```

**View the Code:**
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Option C: C 🔧

```bash
# Navigate to C directory
cd c

# Find the hello_world file
ls | grep hello

# Compile the program
gcc hello_world.c -o hello_world

# Run the program
./hello_world          # Linux/macOS
hello_world.exe        # Windows

# Expected Output:
# Hello, World!
```

**View the Code:**
```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### Option D: C++ 🚀

```bash
# Navigate to C++ directory
cd cpp

# Compile the program
g++ hello_world.cpp -o hello_world

# Run the program
./hello_world

# Expected Output:
# Hello, World!
```

**View the Code:**
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

### Option E: JavaScript/Node.js 📜

```bash
# Navigate to JavaScript directory (if exists)
cd javascript

# Run with Node.js
node hello_world.js

# Expected Output:
# Hello, World!
```

## ✏️ Step 4: Modify the Code

Let's make the program more interactive!

### Python Example

```python
# Edit hello_world.py
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Programming Solutions Universe!")
```

### Run Your Modified Program

```bash
python hello_world.py

# Input: John
# Output: Hello, John! Welcome to Programming Solutions Universe!
```

## 🔍 Step 5: Try a More Complex Problem

### Example: Sum of Two Numbers

**Navigate to a solution:**

```bash
# Python
cd python
python sum_two_numbers.py

# OR Java
cd java
javac SumTwoNumbers.java
java SumTwoNumbers

# OR C
cd c
gcc sum_two_numbers.c -o sum
./sum
```

### Understand the Code

**Python Example:**
```python
# sum_two_numbers.py
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum_result = a + b
print(f"Sum: {sum_result}")
```

**Try it yourself:**
```bash
python sum_two_numbers.py
# Enter first number: 5
# Enter second number: 10
# Sum: 15
```

## 📊 Step 6: View the Status Page

### Open the Interactive Status Tracker

```bash
# Option 1: Open directly in browser
# Double-click status.html in your file explorer

# Option 2: Use command line
# macOS
open status.html

# Linux
xdg-open status.html

# Windows
start status.html
```

### Features to Explore

- 🌓 **Dark/Light Mode Toggle**: Switch between themes
- �� **Progress Tracking**: See completion status for each language
- 🎨 **Animated Splash Screen**: Enjoy the loading animation
- 📱 **Responsive Design**: View on any device
- 🏷️ **Shields.io Badges**: Visual status indicators

## 🔄 Step 7: Generate Updated Status

### Run Automation Scripts

```bash
# Generate fresh HTML status page
python generate_html.py

# Update status tracking
python update_status.py

# View the updated page
open status.html
```

## 🧪 Step 8: Test Multiple Languages

### Challenge: Run the Same Problem in 3 Languages

**Problem**: Print "Hello, World!"

```bash
# Python
cd python && python hello_world.py

# Java
cd ../java && javac HelloWorld.java && java HelloWorld

# C
cd ../c && gcc hello_world.c -o hello && ./hello
```

**Compare**:
- Syntax differences
- Compilation requirements
- Execution speed
- Code verbosity

## 🎓 What You've Learned

Congratulations! You've successfully:

- ✅ Navigated the repository structure
- ✅ Found and read a problem
- ✅ Ran solutions in your language(s)
- ✅ Modified and tested code
- ✅ Viewed the status tracker
- ✅ Used automation scripts

## 🚀 Next Steps

### Beginner Path
1. 📚 Work through [Easy problems](https://raw.githubusercontent.com/DibyajyotiBiswal57/programs/refs/heads/main/questions.md#easy)
2. 🔍 Study [Language-Specific Guides](Language-Guides)
3. 💡 Complete 5 problems in your primary language

### Intermediate Path
1. 🔄 Implement solutions in a new language
2. 🧪 Compare different approaches to the same problem
3. 📝 Solve [Medium difficulty problems](https://raw.githubusercontent.com/DibyajyotiBiswal57/programs/refs/heads/main/questions.md#medium)

### Advanced Path
1. 🏆 Tackle [Hard problems](https://raw.githubusercontent.com/DibyajyotiBiswal57/programs/refs/heads/main/questions.md#hard)
2. 🤝 Contribute new solutions ([Contributing Guide](Contributing))
3. 🛠️ Add support for a new language ([Adding New Language](Adding-New-Language))
4. 📖 Improve documentation

## 💡 Pro Tips

### Efficiency Tips
```bash
# Create aliases for frequent commands
alias pyrun='python'
alias javarun='javac *.java && java'

# Use tab completion
cd prog<TAB>  # Autocompletes to 'programs'
```

### Learning Tips
- 📝 Keep a coding journal of new concepts learned
- 🔄 Try implementing the same solution in different languages
- 💬 Comment your code to solidify understanding
- 🧪 Experiment by breaking and fixing code

### Organization Tips
```bash
# Create a workspace for your modifications
mkdir my-solutions
cp python/hello_world.py my-solutions/

# Track your progress
echo "Completed: Hello World (Python, Java, C)" >> progress.txt
```

## 🐛 Common Issues & Solutions

### Issue: "File not found"
```bash
# Solution: Verify you're in the correct directory
pwd
ls
```

### Issue: "Command not found"
```bash
# Solution: Check if the language is installed
python --version
java --version
gcc --version
```

### Issue: Compilation errors
```bash
# Solution: Check for syntax errors
# Read the error message carefully
# Verify file names match class names (Java)
```

### Issue: Permission denied (Linux/macOS)
```bash
# Solution: Make file executable
chmod +x filename
```

## 📚 Additional Resources

- 🏠 [Back to Home](Home)
- 🛠️ [Installation & Setup](Installation-Setup)
- 🗂️ [Project Structure](Project-Structure)
- ❓ [FAQ](FAQ)
- 🤝 [Contributing](Contributing)

## 🤔 Need Help?

- 💬 [Open a Discussion](https://github.com/DibyajyotiBiswal57/programs/discussions)
- 🐛 [Report an Issue](https://github.com/DibyajyotiBiswal57/programs/issues)
- 📧 Email: coder99957@dibyajyoti.is-a.dev

## 🎉 Congratulations!

You've completed the Quick Start Tutorial! You're now ready to explore the Programming Solutions Universe. Happy coding! 🚀

---

**Last Updated**: 2026-02-07  
**Difficulty**: Beginner  
**Estimated Time**: 15-20 minutes

💡 **Next Tutorial**: [Working with Multiple Languages](Working-With-Multiple-Languages) (Coming Soon!)
```
