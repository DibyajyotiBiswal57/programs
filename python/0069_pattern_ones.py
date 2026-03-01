n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    string = ""
    for u in range(i):
        string += "1 "
    print(string)
