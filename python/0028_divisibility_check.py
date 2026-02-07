print("This program check if a number is divisible by another number.")
num = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num % num2 == 0:
    print(f"{num} is divisible by {num2}.")
else:
    print(f"{num} is not divisible by {num2}.")

