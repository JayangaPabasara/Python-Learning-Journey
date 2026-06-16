# Variables creation and usage

# Assign values to the varibales
# In pythin can't declare avaribale name without a value assign
name = "Jaya"
age = 24
height = 1.75
is_student = True
result = None

# Print varibales values stroed
print("My name is " + name + ".") # using + operator to concatenate in python only can use for string + string 
print(f"I'm {age} years old.") # use f-stinrgs to concatenate - best, modern and no need to convert.
print(height)
print(is_student)
print(result)

# Change varibale values
name = "Jayanga Pabasara"
age = 23
result = f"{name} Weerasinghe"

# Print Changed Values
print(f"My name is {name} and I'm {age} years old.")
print(result)

# Print inline text end= parameter
print("This is my", end=' second code file.')
print()
# print("second code file.") // Both are working

# Use sep= parameter - use to set a speratation attribute
print("Mango", "Banana", "Apple", sep=' | ')