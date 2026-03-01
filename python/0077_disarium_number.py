n = int(input("Enter a number: "))
sum = 0
for i in range(len(str(n))):
    sum += int(str(n)[i]) ** (i + 1)
if sum == n:
    print(f"{n} is a Disarium number.")
else:
    print(f"{n} is not a Disarium number.")
