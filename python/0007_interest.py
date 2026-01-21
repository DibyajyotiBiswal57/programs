#Q7
print("This program calculates the simple interest and amount.")
p=float(input("Enter the principal: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time taken in years: "))

si=p*r*t
amt=si+p

print(f"The simple on {p} for {t} years at {r}% is {si}.")
print(f"The amount is {amt}.")
