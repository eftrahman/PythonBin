# Python Comments
# Comments are lines in Python that start with a "#" symbol.
# Python ignores these lines while running the code.
# Use comments to explain your code or leave reminders for yourself.

# Variables in Python
# A variable stores data that you can use or modify throughout your code.
# You don't need to declare the type; Python figures it out based on the value assigned.

x = 5  # an integer variable
y = "Hello, World!"  # a string variable
print(x)
print(y)

# Variable Names
# Variable names in Python can contain letters, numbers, and underscores, but they can't start with a number.

my_variable = "Python"  # Valid name
_my_var = 42  # Also valid
# 2var = 10  # Invalid: can't start with a number

# Assign Multiple Values
# You can assign multiple values to multiple variables in one line.
a, b, c = "apple", "banana", "cherry"
print(a)
print(b)
print(c)

# Output Variables
# Use the print() function to output the value of variables.

name = "Eftear"
age = 25
print("Name:", name)
print("Age:", age)

# Global Variables
# Variables created outside of functions are global and can be used anywhere in the code.

global_var = "I'm global"

def my_function():
    # If we want to change a global variable inside a function, we need to use the `global` keyword
    global global_var
    global_var = "Changed globally"

print("Before function:", global_var)
my_function()
print("After function:", global_var)

# Python Data Types
# Data types are important in programming to know what kind of value a variable holds.

# Different data types in Python include:
my_int = 10          # int
my_float = 20.5      # float
my_str = "Hello"     # str
my_bool = True       # bool
my_list = [1, 2, 3]  # list
my_tuple = (1, 2, 3) # tuple
my_set = {1, 2, 3}   # set
my_dict = {"name": "Eftear", "age": 25}  # dictionary

print(type(my_int))
print(type(my_float))
print(type(my_str))
print(type(my_bool))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))

# Python Numbers
# There are three types of numbers in Python: int, float, and complex.

num_int = 10      # integer
num_float = 10.5  # float
num_complex = 1j  # complex

print(type(num_int), type(num_float), type(num_complex))

# Python Casting
# Casting is when you convert a variable from one type to another.
# Here are some basic examples:

x = int(1)    # x will be 1
y = float(2)  # y will be 2.0
z = str(3.0)  # z will be '3.0'

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Variable Exercises
# Practice what you've learned! Try creating variables with different types, naming them with different conventions, 
# and using them in simple operations.

# Exercise example:
a = 5
b = "Data Science"
print("a:", a, "| type of a:", type(a))
print("b:", b, "| type of b:", type(b))
