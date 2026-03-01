n = int(input("Enter a number: "))
sqr = n**2

if (sqr - n) % (10 ** (len(str(n)))) == 0:
    print(f"{n} is an Automorphic number.")
else:
    print(f"{n} is not an Automorphic number.")
