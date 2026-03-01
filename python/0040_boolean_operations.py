import math

h = 0
r = 0
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
boolean = input("Enter 'True' or 'False': ").strip().lower() == "true"
if boolean:
    print(f"Area of rectangle is {a * b}")
    print(f"Perimeter of rectangle is {2 * (a + b)}")
else:
    h = a
    r = b
    print(
        f"Surface area of the cylinder is {
            2 *
            math.pi *
            r *
            h +
            2 *
            math.pi *
            r ** 2}")
    print(f"Volume of clyinder is {math.pi * r ** 2 * h}")
