#Q8
print("This program will tell you which number is greater")
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))

if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print("Both numbers are equal")
