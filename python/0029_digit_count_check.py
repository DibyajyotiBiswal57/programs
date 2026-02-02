num = float(input("Enter a number: "))
if num.is_integer():
    if 0 <= abs(num) <= 9:
        print(f"{num} is a 1-digit number.")
    elif 10 <= abs(num) <= 99:
        print(f"{num} is a 2-digit number.")
    elif 100 <= abs(num) <= 999:
        print(f"{num} is a 3-digit number.")
    else:
        print(f"{num} has more than 4 digits.")
else:
    print("ERROR! THIS PROGRAM ONLY SUPPROTS INTEGERS.")
