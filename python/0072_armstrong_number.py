n = int(input("Enter a number: "))
sum = 0
for i in list(str(n)):
    sum += int(i) ** 3
if sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
