n = int(input("Enter a number: "))
print(f"Factorial series upto {n}:")
S = 0
string = ""
for i in range(1,n+1):
    u = 0
    u_string = ""
    d = 0
    d_string = ""
    for a in range(1,i+1):
        u+=a
        u_string+=str(a)+ "+"
    u_string = u_string[0:-1]
    for a in range(1,i+1):
        factorial = 1
        for b in range(1,a+1):
            factorial*=b
        d+=factorial
        d_string += str(a)+ "!+"
    d_string = d_string[0:-1]
    S+=(u/d)
    string += (f"[({u_string})/({d_string})] + ")
string = string[0:-3]
print(string)
print(f"The net resultant is: {S}")
