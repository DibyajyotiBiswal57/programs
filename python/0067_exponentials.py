n = int(input("Enter the number to be exponated: "))
a = int(input("Enter the exponent: "))
total = 1
for i in range(a):
    total *= n
print(f"The answer is {total}.")
