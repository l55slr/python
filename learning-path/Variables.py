# Variables are called "variables" because they can hold any value and that value can change (it varies).
print("Variables assignment:")
player_health = 1000
print(player_health)


# the variable overwriting case:
print("Variable overwriting:")
acceleration = 10
acceleration = 20
print(acceleration)
# The line acceleration = 20 reassigns the value of acceleration to 20.
# It overwrites whatever was being held in the acceleration variable before (10 in this case).


# Math CH, We can also perform math operations on variables. you most follow the order of calculation (PEMDAS) when doing so.
# some commen math operations are:
# addition: +, subtraction: -, multiplication: *, division: /
print("Math with variables:")
player_health = 1000
armor_multiplier = 2
armored_health = player_health * armor_multiplier
print(armored_health)


""""
Variable Names: Variable names must not have spaces, 
and they must not start with a number. 
They can only contain letters, numbers, and underscores.
plus they have two coommon way of naming like camelCase and snake_case.
"""

#Variable Types: Variables can hold different types of data. Some common types include:
# - Integers (whole numbers): e.g., 42, -7
x = 5

# - Floats (decimal numbers): e.g., 3.14, -0.001
x = 5.2

# - Strings (text): e.g., "Hello, World!"
x = "Hello, World!"       

# - Booleans (true/false values): e.g., True, False
is_tall = True
is_short = False


# we can create strings that contain dynamic values with the f-string syntax.
print("F-string example:")
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")


#NoneType Variables
print("NoneType variable example:")
enemy = None
print(enemy is None)


"""
Info:
in one line many variables can be declared on the same line.
"""
