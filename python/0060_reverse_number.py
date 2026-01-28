num = int(input("Enter a number: "))
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10
print("Reversed number:", rev_num)
