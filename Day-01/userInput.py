# input() puses the program and waits for the user to type.

full_name = input("Enter you full name here: ")
age = input("Enter your age here: ")

print("Hello", full_name)
print("You are", age, "years old.") # When a comma is used in print python add a space and also mearge.

# Importent input() is always returning a string. So age aboee is a sting not an intiger
# Convert string to intiger
age_as_number = int(age)
print("Age in number", age_as_number)
