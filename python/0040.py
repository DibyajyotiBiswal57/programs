#Q40
character = input("Enter a character: ")
character = character.lower()
if character in {'a', 'e', 'i', 'o', 'u'}:
    print(f"The character '{character}' is a vowel.")
elif character.isalpha():
    print(f"The character '{character}' is a consonant.")
else:
    print(f"The character '{character}' is not a valid alphabet letter.")
