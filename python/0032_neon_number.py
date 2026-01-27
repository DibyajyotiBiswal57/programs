num = int(input("Enter a number: "))
square = num ** 2
sum_digits = 0

while square > 0:
    digit = square % 10
    sum_digits += digit
    square = square // 10

if sum_digits == num:
    print(f"{num} is a neon number.")
else:
    print(f"{num} is not a neon number.")
