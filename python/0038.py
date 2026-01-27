#Q38
num = float(input("Enter a number: "))
print("Enter 'S' to find square of the number.")
print("Enter 'C' to find cube of the number.")
char = input()
if char == "S":
    print(f"{num**2} is the sqaure of {num}.")
elif char == "C":
    print(f"{num**3} is the cube of {num}.")
else:
    print("Invalid selection.")
    
