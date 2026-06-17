# 🐍 Python Learning Journey

---

## 📅 Day 01 — June 16, 2026

### What I Learned Today

#### 1. Variables
- A variable is a named container that stores a value
- In Python, you **must assign a value when you create a variable**
- Use `None` if you want a variable to exist but have no value yet

```python
name = "Kasun"      # string variable
age = 25            # integer variable
result = None       # empty variable — value to be assigned later
```

#### 2. The `print()` Function
- Displays output on the screen
- By default adds a new line at the end

```python
print("Hello, World!")                        # basic print
print("Hello", end=" ")                       # inline — no new line
print("Kasun", "Perera", "Brisbane", sep="-") # Kasun-Perera-Brisbane
```

**Key `print()` parameters:**
| Parameter | Default | What it does |
|-----------|---------|--------------|
| `end`     | `"\n"`  | Character added at the end |
| `sep`     | `" "`   | Character placed between values |

#### 3. The `input()` Function
- Pauses the program and waits for the user to type something
- ⚠️ **Always returns a string** — convert it if you need a number

```python
name = input("What is your name? ")     # returns a string
age  = input("How old are you? ")       # also a string — even if user types 25

age_as_number = int(age)                # convert to int before doing math
```

---

### ✅ Today's Progress
- [x] Wrote my first Python program
- [x] Learned variable declaration and value assignment
- [x] Understood `print()` with `end=` and `sep=` parameters
- [x] Learned about `None` value
- [x] Learned `input()` function and its string return behaviour

---

### 💡 Key Reminder
> `input()` **always** returns a string, even when the user types a number.
> Always use `int()` or `float()` to convert before doing any calculations.

---

## 📅 Day 02 — June 17, 2026

### What I Learned Today

    - Type Conversion

### What I Practiced Today

Completed all three Week 1 exercises from Phase 1 — Python Fundamentals.

#### Exercise 1 — Personal Information Card
Stored personal details (name, age, height, city) using the correct data types and printed them in a clean, readable format.

```python
first_name = "Kasun"
last_name = "Perera"
age = 25
height = 1.75
city = "Brisbane"

print("----- My Information -----")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Height: {height} metres")
print(f"City: {city}")
```

**Key takeaway:** Using the correct data type for each variable (`str`, `int`, `float`) matters — it's not just style, it affects what operations you can do with the value later.

---

#### Exercise 2 — Age Calculator
Used `input()` to get the user's birth year, converted it to an integer, and calculated their current age and the year they turn 30.

```python
birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)          # convert string to int

age = 2024 - birth_year
year_turning_30 = birth_year + 30

print(f"You are {age} years old.")
print(f"You will turn 30 in {year_turning_30}.")
```

**Key takeaway:** `input()` always returns a string — forgetting to convert it with `int()` before doing math is one of the most common beginner mistakes.

---

#### Exercise 3 — Type Detective
Explored how `type()` works and tested type conversion between `int`, `float`, `str`, and `bool`.

```python
number_1 = 100
number_2 = 100.0
word = "100"
flag = True

print(type(number_1))   # <class 'int'>
print(type(number_2))   # <class 'float'>
print(type(word))       # <class 'str'>
print(type(flag))       # <class 'bool'>

print(float(number_1))  # 100.0
print(int(number_2))    # 100
print(str(number_1))    # "100"

print(int(flag))        # 1  — surprising! True converts to 1, False converts to 0
```

**🔍 Surprising discovery:** `int(True)` returns `1` and `int(False)` returns `0`. This is because in Python, booleans are technically a subtype of integers behind the scenes.

---

### ✅ Today's Progress
- [x] Exercise 1 — Personal Information Card
- [x] Exercise 2 — Age Calculator
- [x] Exercise 3 — Type Detective

---

### 💡 Key Reminder
> Always check the data type of a variable before performing operations on it — especially after using `input()`, since it always returns a string.

---

