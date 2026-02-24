import random
print("Welcome to the Guessing Game!")
u = int(input("Enter the upper limit for selecting numbers: "))
n = random.randint(1,u)
print(f"\nGuess a number from 1 to {u}.")
ans = 0
i = 0
while ans!=n:
    ans=int(input("Type your guess: "))
    i+=1
    if ans > n: print("Your guess is higher than the number.")
    elif ans<n: print("Your guess is lower than the number.")
    else:
        print("Congratulations! You have won!")
        print(f"You took {i} turns.")