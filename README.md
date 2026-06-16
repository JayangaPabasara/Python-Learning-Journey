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
