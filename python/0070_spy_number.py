n = str(int(input("Enter a number: ")))
product = 1
sum = 0
for i in range(len(n)):
    product*=int(n[i])
    sum+=int(n[i])
if product==sum:
    print(f"{n} is a spy number.")
else:
    print(f"{n} is not a spy number.")