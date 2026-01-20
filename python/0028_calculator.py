#Q28
print("This is a calculator")
print()
print("ENter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for division")
print("Enter % for modulus")
print("Enter ^ for power")
operator = input()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operator == "+":
    print("The sum is: ", num1 + num2)
elif operator == "-":
    print("The difference is: ", num1 - num2)
elif operator == "*":
    print("The product is: ", num1 * num2)
elif operator == "/":
    print("The quotient is: ", round(num1 / num2, 3))
elif operator == "%":
    print("The modulus is: ", num1 % num2)
elif operator == "^":
    print("The power is: ", num1 ** num2)
else:
    print("Invalid operator")
