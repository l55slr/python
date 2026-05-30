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
print("Math with variables:")
player_health = 1000
armor_multiplier = 2
armored_health = player_health * armor_multiplier
print(armored_health)


