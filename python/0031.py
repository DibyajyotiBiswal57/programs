#Q31
num = str(input("Enter a number: "))
if num[::1] == num[::-1]:
    print(f"{num} is a palindromic number.")
else:
    print(f"{num} is a not palindromic number.")
