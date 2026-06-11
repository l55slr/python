#lists: A natural way to organize and store data is in a List, 
#Lists in Python are declared using square brackets, with commas separating each item:
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]


#Lists Continued: Sometimes when we're manually creating lists it can be hard to read if all the items are on the same line of code.
#We can declare the list using multiple lines if we want to:
inventory = [
    "Iron Breastplate",
    "Healing Potion",
    "Leather Scraps"
]


#Counting in Programming: We don't start counting at 1, we start at 0 instead.
inventory = [
    "Iron Breastplate",
    "Healing Potion",
    "Leather Scraps"
]
#Iron Breastplate: index 0
#Healing Potion: index 1
#Leather Scraps: index 2


#List Length: List can be calculated using the len()
fruits = ["apple", "banana", "pear"]
length = len(fruits)


#Here we used -1 because the list reads the lenght starting from 1 not 0, so the last index is always one less than the length of the list.
def get_last_index(inventory):
    length = len(inventory)
    return len(inventory) -1


#list update: We can change the value of an item in a list by using its index and assigning it a new value:
def smelt_ore(inventory):
    if inventory [1] == "Iron Ore":
        inventory [1] = "Iron Bar"
    return inventory



#Appending in Python: We can add items to the end of a list using the append() method:
cards = []
cards.append("nvidia")
cards.append("amd")
print(cards)


#pop value: We can remove the last item from a list using the pop() method:
cards = ["nvidia", "amd", "intel"]
cards.pop()
print(cards)