#Q16
print("Weird operations")
num=int(input("Enter a number: "))

if num < 100 or num > 999:
    print("Invalid number.")
else:
    num1 = num // 100
    num2 = (num % 100) // 10
    num3 = num % 10
    add=num1+num2
    mul=num1*num3
    print(f"The sum of the first and second digits is: {add}")
    print(f"The product of the first and second digits is: {mul}")
