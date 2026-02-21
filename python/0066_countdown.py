import time

i = int(input("Enter a number: "))

for j in range(i, 0, -1):
    print(j)
    time.sleep(1)