#Q18

m = int(input("Enter a number: "))
n = int(input("Enter a number: "))

if m > n:
    while n < m - 1:
        n = n + 1
        if n % 2 == 1:
            print(n)

elif m == n:
    print("Nothing to print as both values are equal.")

elif m < n:
    while m < n - 1:
        m = m + 1
        if m % 2 == 1:
            print(m)
