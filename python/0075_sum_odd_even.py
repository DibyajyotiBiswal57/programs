n= int(input("Enter a number: "))
odd = 0
even = 0

for i in range(1,n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f"Sum of odd numbers: {odd}")
print(f"Sum of even numbers: {even}")