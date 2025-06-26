# Week 1 - Python Basics
# Topics: Variables, Loops, Functions, Conditionals

# 1. Variables and Data Types
name = "Sumit"
age = 20
height = 5.9
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# 2. Conditional Statements
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("Just turned adult!")
else:
    print("You are an adult.")

# 3. Loops
# For Loop
print("Numbers from 1 to 5 using for loop:")
for i in range(1, 6):
    print(i)

# While Loop
print("Numbers from 5 to 1 using while loop:")
count = 5
while count > 0:
    print(count)
    count -= 1

# 4. Functions
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

print(greet("AI/ML Learner"))
print("Sum of 10 and 15 is:", add_numbers(10, 15))

# 5. Lists and Loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# 6. Dictionary
student = {
    "name": "Sumit",
    "course": "AI/ML",
    "year": 2025
}
print("Student Details:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
