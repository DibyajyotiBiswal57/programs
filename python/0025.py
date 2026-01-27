#Q25
print("This program calculates the perimeter of a rectangle, square, triangle, circle, parallelogram.")
print("Enter the shape for which you want to calculate the perimeter:")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")
print("4. Circle")
print("5. Parallelogram")
shape = int(input("Enter the shape: "))
if shape == 1:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    perimeter = 2 * (length + breadth)
    print("The perimeter of the rectangle is", perimeter)
elif shape == 2:
    side = float(input("Enter the side of the square: "))
    perimeter = 4 * side
    print("The perimeter of the square is", perimeter)
elif shape == 3:
    side1= float(input("Enter the first side of the triangle: "))
    side2= float(input("Enter the second side of the triangle: "))
    side3= float(input("Enter the third side of the triangle: "))
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is", perimeter)
elif shape == 4:
    radius = float(input("Enter the radius of the circle: "))
    perimeter = 2 * 3.14159 * radius
    print("The perimeter of the circle is", perimeter)
elif shape == 5:
    side1 = float(input("Enter the first side of the parallelogram: "))
    side2 = float(input("Enter the second side of the parallelogram: "))
    perimeter = 2 * (side1 + side2)
    print("The perimeter of the parallelogram is", perimeter)
else:
    print("Invalid shape entered.")
