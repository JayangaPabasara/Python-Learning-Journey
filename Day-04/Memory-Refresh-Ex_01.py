# BMI = weight (kg) / height (m) squared
# Ask the user for their name, weight, and height
# Calculate their BMI
# Use if/elif/else to print the category:
#   Below 18.5 = Underweight
#   18.5 to 24.9 = Normal weight
#   25 to 29.9 = Overweight
#   30 and above = Obese
# Print a personalised message using an f-string

# Example output:
# Hello Kasun! Your BMI is 22.9 — Normal weight. Keep it up!

print("============BMI Calculator============")

name = ""
weight = ""
height = ""

while not name or not weight or not height:
    print("---Please Enter Your Details To Continue---")
    name = input("Enter your first name here: ")
    weight = input("Enter your weight in kilogram: ")
    height = input("Enter your height in meter: ")
    
    if not name or not weight or not height:
        print("⚠️  All fields are required! Please fill in everything.\n")

weight = float(weight)
height = float(height)

BMI = weight / height ** 2

print(f"Hello {name}!", end=" ")

if BMI < 18.5:
    print(f"Your BMI is {BMI:.1f} - Underweight.")
elif BMI <= 24.9:
    print(f"Your BMI is {BMI:.1f} - Normal weight. Keep it up!")
elif BMI <= 29.9:
    print(f"Your BMI is {BMI:.1f} - Overweight.")
else:
    print(f"Your BMI is {BMI:.1f} - Obese.")

# {BMI:.1f}
#     ^         → : means "format this value as..."
#      ^        → . means "decimal places"
#       ^       → 1 means "show 1 decimal place"
#        ^      → f means "this is a float number"