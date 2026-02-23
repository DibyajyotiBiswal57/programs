n = int(input("Enter a number: "))

i = 1
row = 1
while i <= n:
    
    List = []
    while i <= n:
        List.append(str(i))
        i += 1
        if len(List)>= row:
            break
    row += 1
    string = ""
    for i in range(len(List)):
        string += (List[i] + " ")
    print (string)