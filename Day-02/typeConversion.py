# Converting between types

number_as_text = "45"
print(type(number_as_text))

number = int (number_as_text)
print(type(number))

decimal = float(number_as_text)
print(type(decimal))

# Useful when you want to join a number with text
age = 25

message = "I am " + str(age) + " years old"
print(message)