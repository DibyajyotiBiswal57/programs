Input "Enter a number: ", a
Input "Enter a number: ", b
Input "Enter a number: ", c
Print ""
Print "The numbers entered are: "
Print a; b; c

a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)

Print""
Print "The swapped numbers are:"
Print a; b; c
