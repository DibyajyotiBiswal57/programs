num = int(input("Enter anumber: "))
i = 1
fact = 1
while i < num:
    fact = fact * i
    i = i + 1

print(f"The factorial of {num} is {fact}.")
