string = list(input("Enter a string:\n"))
for i in range(len(string)):
    if string[i] == string[i].lower():
        string[i] = string[i].upper()
    elif string[i] == string[i].upper():
        string[i] = string[i].lower()

print("The toggled string is:\n" + "".join(string))
