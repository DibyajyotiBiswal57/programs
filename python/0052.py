#Q52
# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Print the original numbers
print("Original numbers:")
print("First number:", num1)
print("Second number:", num2)
print("Third number:", num3)

# Swap the numbers
temp = num1
num1 = num2
num2 = num3
num3 = temp

# Print the swapped numbers
print("\nSwapped numbers:")
print("First number (now second):", num1)
print("Second number (now third):", num2)
print("Third number (now first):", num3)
