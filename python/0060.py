#Q60

num = int(input("Enter a number: "))
counter = 0
i = 1
while i < num:
    if num % i == 0:
        counter += 1
    i += 1
if counter > 2:
    print("It is not a prime number.")
else:
    print("It is a prime number.")
