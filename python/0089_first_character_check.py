string = str(input("Enter the string:\n"))
charList = []
for i in range(len(string)):
    if string[i] == " " and string[i + 1].isalpha():
        charList.append((string[i + 1]).lower())

while True:
    char = str(input("Enter the character to check: ")).lower()
    if len(char) == 1 and char.isalpha():
        break
    else:
        print("Please enter a single alphabetic character.")

print(
    f'The letter "{
        char.upper()}" appears {
            charList.count(char)} times as the first letter of a word.')
