num = int(input("Enter a number: "))
a = int(input("Enter the divisor: "))
if num % a == 0:
    print(f"{num} is divisible by {a}.")
else:
    print(f"{num} is not divisible by {a}.")