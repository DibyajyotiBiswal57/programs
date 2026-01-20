#Q4 & 5
import math

print("This program calculates the area and volume of some shapes.")
choice1=input("Enter '1' for area for some shapes, '2' for the volume for some shapes: ")

if choice1=='1':
    print()
    print("Enter '1' for area of a square")
    print("Enter '2' for area of a rectangle")
    print("Enter '3' for area of a circle")
    print("Enter '4' for area of a triangle")
    print("Enter '5' for area of a parallelogram")
    print("Enter '6' for area of a rhombus")
    print("Enter '7' for area of a trapezium")
    choice2=input("Enter your choice: ")

    if choice2=='1':
            
            # Area of a square
            side=float(input("Enter the side of the square: "))
            area=side**2
            print(f"The area of the square is {area}.")

    elif choice2=='2':

            # Area of a rectangle
            len=float(input("Enter the length of the rectangle: "))
            bre=float(input("Enter the breadth of the rectangle:"))

            area=len*bre

            print(f"The area of the rectangle is {area}.")

    elif choice2=='3':

            # Area of a cirle
            rad=float(input("Enter the radius of the circle: "))

            area = math.pi*rad**2

            area = round(area, 2)

            print(f"The area of the circle is approximately {area}.")

    elif choice2=='4':
            
            # Area of a triangle

            base=float(input("Enter the base of the triangle: "))
            height=float(input("Enter the height of the triangle: "))

            area=0.5*base*height

            print(f"The area of the triangle is {area}.")

    elif choice2=='5':
            
            # Area of a parallelogram
            base=float(input("Enter the base of the parallelogram: "))
            height=float(input("Enter the height of the parallelogram: "))

            area=base*height

            print(f"The area of the parallelogram is {area}.")

    elif choice2=='6':

            # Area of a rhombus
            dia1=float(input("Enter the first diagonal of the rhombus: "))
            dia2=float(input("Enter the second diagonal of the rhombus: "))

            area=0.5*dia1*dia2

            print(f"The area of the rhombus is {area}.")

    elif choice2=='7':

            # Area of a trapezium
            a=float(input("Enter the length of the first parallel side: "))
            b=float(input("Enter the length of the second parallel side: "))
            height=float(input("Enter the height of the trapezium: "))

            area=0.5*(a+b)*height

            print(f"The area of the trapezium is {area}.")

    else:
            print("Invalid input. Please enter a valid input.")

elif choice1=='2':

    print()
    print("Enter '1' for volume of a cube")
    print("Enter '2' for volume of a cuboid")
    print("Enter '3' for volume of a sphere")
    print("Enter '4' for volume of a cylinder")
    print("Enter '5' for volume of a cone")
    choice2=input("Enter your choice: ")

    if choice2=='1':
        
        # Volume of a cube
        side=float(input("Enter the side of the cube: "))

        volume=side**3

        print(f"The volume of the cube is {volume}.")

    elif choice2=='2':

        # Volume of a cuboid
        len=float(input("Enter the length of the cuboid: "))
        bre=float(input("Enter the breadth of the cuboid: "))
        height=float(input("Enter the height of the cuboid: "))

        volume=len*bre*height

        print(f"The volume of the cuboid is {volume}.")

    elif choice2=='3':

        # Volume of a sphere
        rad=float(input("Enter the radius of the sphere: "))

        volume=4/3*math.pi*rad**3

        volume=round(volume, 2)

        print(f"The volume of the sphere is approximately {volume}.")

    elif choice2=='4':

        # Volume of a cylinder
        rad=float(input("Enter the radius of the cylinder: "))
        height=float(input("Enter the height of the cylinder: "))

        volume=math.pi*rad**2*height

        volume=round(volume, 2)

        print(f"The volume of the cylinder is approximately {volume}.")

    elif choice2=='5':

        # Volume of a cone
        rad=float(input("Enter the radius of the cone: "))
        height=float(input("Enter the height of the cone: "))

        volume=1/3*math.pi*rad**2*height

        volume=round(volume, 2)

        print(f"The volume of the cone is approximately {volume}.")

    else:
        print("Invalid input. Please enter a valid input.")

else:
    print("Invalid input. Please enter a valid input.")
