i = int(input("Enter number of rows: "))
for a in range(i, 0, -1):                       # Loop for each row
    string = ""                                 # Start with an empty string
    for b in range(a):                          # Constructing a row
        string = string + " " + str(b+1)          # Row to have all numbers till 'u'
    print(string)                               # Print the row