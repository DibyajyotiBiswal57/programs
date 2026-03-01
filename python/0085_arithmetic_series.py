n = int(input("Enter the numer of terms: "))
a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))

string = ""
sum = 0
for i in range(a, (a + (n * d)), d):
    string += str(i) + " "
    sum += i
print("The Arithmetic series is: " + string)
print("Sum: " + str(sum))
