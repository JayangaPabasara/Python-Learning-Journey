age = 20
has_id = True

# 'and' both condition must be True
print(age >= 18 and has_id == True)
print(age >= 18 and age < 18)

# 'or' at least on condition must bee True
print(age >= 18 or age < 10)
print(age < 18 or age > 100)

# 'not' reverse True to False and False to True
print(not True)
print(not False)
print(not age > 18 or has_id == True)