i = 0
num = int(input("Enter a number: "))
while i < num:
    if i % 3 == 0 and i % 7 == 0:
        print(f"{i} is divisible by 3 and 7.")
    i = i + 1
