# Ask the user to enter a number between 1 and 20
# Validate the input using a while loop:
#   if the number is outside 1-20, print an error and ask again
#   keep asking until they enter a valid number
# Once valid, use a for loop to print the full multiplication table (1x to 12x)

# Example output:
# Enter a number (1-20): 25
# Invalid! Please enter a number between 1 and 20.
# Enter a number (1-20): 5
# ----- Multiplication Table for 5 -----
# 5 x 1  = 5
# 5 x 2  = 10
# ...
# 5 x 12 = 60

print("===========Multiplication Table Generator===========")

isTrue = True
number = None

while isTrue:
    number = input("Enter a number inbetween 1 and 20: ")
    number = int(number)
    if number >= 1 and number <=20:
        isTrue = False
    else:
        print("Please Enter Number Inbetween 1 and 20...!")

for i in range(12):
    print(f"{number} X {i + 1} = {number * (i + 1)}")

