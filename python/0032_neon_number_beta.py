#Q32
num = int(input("Enter a number: "))
digit3 = num % 10
if num % 9 == 0 or digit3 == 9:
    print(f"{num} is a neon number.")
else:
    print(f"{num} is not a neon number.")
