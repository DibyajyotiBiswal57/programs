#Q43
string = input("Enter a string: ")
if string[::1] == string[::-1]:
    print(f"'{string}' is a palidrone.")
else:
    print(f"'{string}' is not a palidrone.")
