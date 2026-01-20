#Q47

str = input("Enter a character: ")
if len(str) > 1:
    print("Aborting program. Character expected, string found.")
else:
    if str == str.upper():
        print(f"{str} is uppercase.")
    elif str == str.lower():
        print(f"{str} is lowercase.")
    else:
        print("Invalid charcter. Please try again.")
