p = 0
r = 0
t = 0
print("1. Simple Interest \n 2. Compound Interest")
choice = int(input("Enter your choice: "))
if choice == 1:
    p = float(input("Enter the principal: "))
    r = float(input("Enter the rate of interest p.a.: "))
    t = float(input("Enter the time taken in years: "))
    si = p * r * t / 100
    amt = si + p
    print(f"The simple interest on {p} for {t} years at {r}% is {si}.")
    print(f"The amount is {amt}.")
elif choice == 2:
    p = float(input("Enter the principal: "))
    r = float(input("Enter the rate of interest p.a.: "))
    t = float(input("Enter the time taken in years: "))
    a = p(1 + r / 100) ** t
    ci = a - p
    print(f"The compound interset on {p} for {t} years at {r}% p.a. is {ci}.")
    print(f"The amount is {a}.")
else:
    print("Invalid choice.")
