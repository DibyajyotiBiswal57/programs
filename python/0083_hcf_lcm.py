a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

A = []
B = []
hcf = 0
for i in range(1, (a//2)+1):
    if a % i == 0:
        A.append(i)
for i in range(1, (b//2)+1):
    if b % i == 0:
        B.append(i)
i = 1
while hcf == 0:
    if A[-1*(i)] in B:
        hcf = A[-1*(i)]
    else:
        i += 1
lcm = int((a*b)/hcf)
print (f"HCF of {a} and {b} is: {hcf}")
print (f"LCM of {a} and {b} is: {lcm}")