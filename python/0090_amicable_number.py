a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum = 0
for i in range(1, (a//2)+1):
    if a % i == 0:
        sum+=i
if sum==b:
    print(f"{a} and {b} are Amicable numbers.")
else:
    print(f"{a} and {b} are not Amicable numbers.")