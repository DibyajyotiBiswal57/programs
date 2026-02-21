a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")