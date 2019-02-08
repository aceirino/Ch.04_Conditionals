print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a":
    sensitivity = 1000
    print("sensitivity: 1000")
elif user_input.lower() == "b":
    sensitivity = 900
    print("sensitivity: 900")
elif user_input.lower() == "c":
    sensitivity = 0
    print("sensitivity: 0")
