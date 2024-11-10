# Basic string input
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Integer input
age = int(input("Enter your age: "))  # Convert the input to an integer
print("You are", age, "years old.")

# Float input
height = float(input("Enter your height in meters (e.g., 1.75): "))  # Convert the input to a float
print("Your height is:", height, "meters.")

# Boolean input
# To simulate a boolean input, we can check if the response is "yes" or "no"
likes_python = input("Do you like Python? (yes/no): ").strip().lower() == "yes"
print("Likes Python:", likes_python)

# List input (using split method to enter multiple items in one line)
# Example input: "apple orange banana"
fruits = input("Enter some favorite fruits separated by space: ").split()
print("Your favorite fruits are:", fruits)

# Tuple input
# Example input: "5, 10, 15"
tuple_input = tuple(map(int, input("Enter numbers separated by commas for a tuple: ").split(',')))
print("Your tuple:", tuple_input)

# Dictionary input (for advanced user input)
# We'll prompt the user to enter key-value pairs in a specific format
print("Let's create a dictionary.")
num_pairs = int(input("How many items do you want to add to the dictionary? "))
user_dict = {}
for i in range(num_pairs):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value for {key}: ")
    user_dict[key] = value
print("Your dictionary:", user_dict)

# Complex data type: Nested dictionary input
print("Let's create a nested dictionary for some extra practice.")
nested_dict = {}
for i in range(2):
    sub_dict = {}
    key = input(f"Enter main key {i + 1}: ")
    for j in range(2):
        sub_key = input(f"Enter sub-key {j + 1} for {key}: ")
        sub_value = input(f"Enter value for {sub_key}: ")
        sub_dict[sub_key] = sub_value
    nested_dict[key] = sub_dict
print("Your nested dictionary:", nested_dict)

