i = int(input("Enter number of rows: "))
u=i
for a in range(i):                              # Loop for each row
    string = ""                                 # Start with an empty string
    for b in range(u):                          # Constructing a row
        string = str(b+1) + " " + string        # Row to have all numbers till 'u'
    print(string)                               # Print the row
    u-=1                                        # Each row is smaller than previous

