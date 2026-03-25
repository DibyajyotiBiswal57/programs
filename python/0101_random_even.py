import random

while true:
    num = random.randint(10,50)
    if num % 2 == 0:
        break
print(f"Random number: {num}")
