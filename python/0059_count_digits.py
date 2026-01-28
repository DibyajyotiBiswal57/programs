num = abs(int(input("Enter a number: ")))
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1
print("Number of digits:", count)
