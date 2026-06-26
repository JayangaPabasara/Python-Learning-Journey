#---------- For Loop -----------#

# Loop using range()
for i in range(5):
    print("Repetition number:", i)

print()

# Loop from 1 to 10
for number in range(1, 11):
    print(number)

print()

# Loop oveer a list of items
fruits = ["appl", "banna", "mango"]
for fruits in fruits:
    print("I like", fruits)

print()

# Print multipication table for 5
for i in range(5):
    result = 5 * i
    print(f"5 X {i} = {result}")



#------------While Loop-----------#

print()

#Basic While loop
count = 1

while count <= 5:
    print("Count: ", count)
    count = count + 1  # Also += operators are working.


print()

# Keep asking until the user types the right answer
password = "python123"
guess = ""

while guess != password:
    guess = input("Enter the password: ")
    if guess != password:
        print("Worng! Try agin.")

print("Access Granted!")

# Break and Continue

print()

# break - stop the loop early
for number in range(1, 11):
    if number == 6:
        break
    print(number)
print("End.")

print()

# continue - skip thee round but keep going
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)