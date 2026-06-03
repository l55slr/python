""""
print() is a function that:
Prints a value to the console
Does not return a value

return is a keyword that:
Ends the current function's execution
Provides a value (or values) back to the caller of the function
Does not print anything to the console (unless the return value is later print()ed)
"""


"""
Multiple Return Values
A function can return more than one value by separating them with commas.
"""
#like this one
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values


"""
Parameters vs. Arguments
Parameters:
are the names used for inputs when defining a function
Arguments:
are the values of the inputs supplied when a function is called.
"""
# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)


#Enchant and Attack
#The function part is my own coding line 41-45
def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage +10
    new_health = target_health - enchanted_damage
    enchanted_weapon = "enchanted" + weapon
    return enchanted_weapon, new_health

def test(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage}... Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()