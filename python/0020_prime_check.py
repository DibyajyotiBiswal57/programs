count = 0
i = 1
num = int(input("Enter a number: "))
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 2:
    print("The number is prime.")
else:
    print("the number is composite.")
print(count)
