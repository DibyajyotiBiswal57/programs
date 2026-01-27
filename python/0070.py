#Q70

num = int(input("Enter a number: "))
print("(1) find the square of the number: ")
print("(2) find the cube of the number: ")
print("(3) Exit: ")
choice = int(input("Enter you choice: "))
if choice == 1:
    print(f"The square of the number is {num**2}")
elif choice == 2:
    print(f"The cube of the number is {num**3}")
elif choice == 3:
    print("Exiting the program.")
else:
    print("Invalid choice.")

