while True:
    char = str(input("Enter a character: "))
    if len(char) == 1 and char.isalpha():
        break
    else:
        print("Please enter a single alphabetic character.")
if char.upper() == char:
    print("The character you entered is in Upper Case.")
else:
    print("The character you entered is in Lower Case.")
