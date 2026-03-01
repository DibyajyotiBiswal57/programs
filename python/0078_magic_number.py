n = int(input("Enter a number: "))
u = n
sum = n
while sum != sum % 10:
    sum = 0
    for i in list(str(u)):
        sum += int(i)
    u = sum
if sum == 1:
    print(f"{n} is a Magic number.")
else:
    print(f"{n} is not a Magic number.")
