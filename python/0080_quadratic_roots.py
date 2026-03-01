a = float(input("Enter the coefficient of x²:- "))
while a == 0:
    a = float(input("The coefficient of x² can't be zero. Please retype:- "))
b = float(input("Enter the coefficient of x:- "))
c = float(input("Enter the coefficient of 1:- "))


dis = b**2 - 4 * a * c
print("")
if dis > 0:
    print("The roots are two distinct real numbers.")
elif dis == 0:
    print("This equation has only one root.")
else:
    print("The roots of this equation are non-real complex numbers.")

if dis >= 0:  # Roots are printed only if they are real
    alpha = str((-1 * b + dis**0.5) / (2 * a))
    beta = str((-1 * b - dis**0.5) / (2 * a))
    print("")
    if alpha != beta:
        print("The roots of the equation are " + alpha + " & " + beta)
    else:
        print("The root of the equation is " + alpha)
