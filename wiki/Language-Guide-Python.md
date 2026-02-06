# Language Guide: Python

## Overview

Python is one of the most popular languages in this repository, with solutions for the majority of problems. It's an excellent choice for beginners due to its readable syntax and extensive standard library.

## Installation

### Windows
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer (check "Add Python to PATH")
3. Verify: `python --version`

### macOS
```bash
# Using Homebrew
brew install python3

# Verify
python3 --version
```

### Linux
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3

# Fedora
sudo dnf install python3

# Verify
python3 --version
```

## Running Python Programs

### Basic Execution
```bash
cd python
python 0001_hello_world.py
# or
python3 0001_hello_world.py
```

### With Input
```bash
# Interactive input
python 0002_sum_of_three.py

# From file
python program.py < input.txt
```

### With Arguments
```bash
python program.py arg1 arg2
```

## Python Coding Style

### Follow PEP 8
- 4 spaces for indentation (not tabs)
- Maximum line length: 79 characters
- Use snake_case for variables and functions
- Use PascalCase for classes

### Example Structure
```python
"""
Problem #XX: Problem Title
Filename: 0000_filename.py

Description:
Brief description of what the program does.

Input: Description of input
Output: Description of output

Example:
Input: 5
Output: 10
"""

# Import statements (if needed)
import math

# Main code
def main():
    # Get input
    n = int(input("Enter a number: "))
    
    # Process
    result = n * 2
    
    # Output
    print(result)

# Entry point
if __name__ == "__main__":
    main()
```

## Common Patterns

### Input Handling
```python
# Single integer
n = int(input())

# Multiple integers on one line
a, b, c = map(int, input().split())

# List of integers
numbers = list(map(int, input().split()))

# String input
text = input()

# Float input
x = float(input())
```

### Output Formatting
```python
# Basic print
print("Hello World")

# Multiple values
print(a, b, c)

# Formatted string
print(f"Result: {result}")

# Without newline
print("Hello", end="")

# With custom separator
print(a, b, c, sep=", ")
```

### Loops
```python
# For loop - range
for i in range(10):
    print(i)

# For loop - list
for item in items:
    print(item)

# While loop
while condition:
    # code

# Loop with enumerate
for index, value in enumerate(items):
    print(f"{index}: {value}")
```

### Conditionals
```python
# If-elif-else
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Ternary operator
result = value1 if condition else value2
```

### String Operations
```python
# Length
length = len(string)

# Concatenation
result = str1 + str2

# Slicing
substring = string[start:end]

# Methods
upper = string.upper()
lower = string.lower()
reversed_str = string[::-1]
```

### List Operations
```python
# Create list
numbers = [1, 2, 3, 4, 5]

# Append
numbers.append(6)

# Length
size = len(numbers)

# List comprehension
squares = [x**2 for x in range(10)]

# Sorting
numbers.sort()  # in-place
sorted_list = sorted(numbers)  # new list
```

## Problem-Specific Tips

### Mathematical Operations
```python
# Power
result = base ** exponent
result = pow(base, exponent)

# Absolute value
abs_value = abs(number)

# Max/Min
maximum = max(a, b, c)
minimum = min(a, b, c)

# Sum
total = sum([1, 2, 3, 4, 5])
```

### Pattern Printing
```python
# Number pattern
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

# Star pattern
for i in range(n):
    print("*" * (i + 1))
```

### String Manipulation
```python
# Palindrome check
is_palindrome = string == string[::-1]

# Count vowels
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)

# Word count
word_count = len(string.split())
```

### Number Theory
```python
# Prime check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Factorial
import math
factorial = math.factorial(n)

# GCD
import math
gcd = math.gcd(a, b)
```

## Best Practices

### 1. Use Descriptive Names
```python
# Bad
n = int(input())

# Good
number = int(input("Enter a number: "))
```

### 2. Add Comments
```python
# Calculate the sum of digits
digit_sum = sum(int(d) for d in str(number))
```

### 3. Handle Edge Cases
```python
# Check for zero division
if denominator != 0:
    result = numerator / denominator
else:
    print("Error: Division by zero")
```

### 4. Use Functions
```python
def calculate_factorial(n):
    """Calculate factorial of n."""
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)
```

### 5. Follow Python Idioms
```python
# Pythonic way to swap
a, b = b, a

# Pythonic way to check multiple conditions
if value in [1, 2, 3, 4, 5]:
    # code

# Use list comprehensions
squares = [x**2 for x in range(10)]
```

## Common Pitfalls

### 1. Integer Division
```python
# Python 3 uses true division
result = 5 / 2  # 2.5

# For integer division, use //
result = 5 // 2  # 2
```

### 2. Mutable Default Arguments
```python
# Bad
def append_to(element, lst=[]):
    lst.append(element)
    return lst

# Good
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

### 3. Input Type Conversion
```python
# Always convert input()
number = int(input())  # Not just input()
```

## Useful Modules

### Standard Library
```python
import math          # Mathematical functions
import random        # Random number generation
import sys           # System-specific parameters
import itertools     # Iterator functions
import collections   # Specialized container datatypes
```

### For Specific Problems
```python
# Permutations and combinations
from itertools import permutations, combinations

# Counter for frequency
from collections import Counter

# Default dictionary
from collections import defaultdict

# Decimal for precise arithmetic
from decimal import Decimal
```

## Examples from Repository

### Problem #1: Hello World
```python
print("Hello World")
```

### Problem #3: Average of Marks
```python
# Input four subject marks
m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))
m4 = float(input("Enter mark 4: "))

# Calculate average
average = (m1 + m2 + m3 + m4) / 4

# Display result
print(f"Average: {average}")
```

### Problem #20: Prime Check
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
```

## Resources

### Official Documentation
- [Python.org](https://www.python.org/)
- [Python Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

### Learning Resources
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Learn Python](https://www.learnpython.org/)
- [Real Python](https://realpython.com/)

### Tools
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [PyCharm IDE](https://www.jetbrains.com/pycharm/)
- [Online Python Compiler](https://www.programiz.com/python-programming/online-compiler/)

## Next Steps

1. Browse Python solutions in `/python` folder
2. Try solving problems yourself before looking at solutions
3. Compare your solution with the repository's
4. Contribute missing solutions!

---

[← Back to Language Guides](Language-Guides) | [Java Guide →](Language-Guide-Java)
