#Q44
str = input("Enter a string: ").lower()
count = 0
for i in str:
    if i in 'aeiou':
        count += 1
print("Number of vowels:", count)
