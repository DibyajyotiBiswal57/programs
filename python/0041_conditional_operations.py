char = input("Enter a character: ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
if char == "a":
    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")
elif char == "M":
    if num1 % 9 == 0:
        print(f"{num1} is divisible by 9")
    else:
        print(f"{num1} is not divisible by 9")
else:
    print(f"Product of {num1} and {num2} is {num1 * num2}")
