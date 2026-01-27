#Q17
print("This program takes a 3 digit number and reverses its digits.")
num = int(input("Enter a number: "))

if num < 100 or num > 999:
    print("Invalid number.")
else:
    num1 = num // 100
    num2 = (num % 100) // 10
    num3 = num % 10
    print(f"The reversed number is: {num3}{num2}{num1}")
