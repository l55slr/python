#A "for loop" in Python is written like this:
for i in range(0, 10):
    print(i)
#this will print the numbers from 0-9 because the range function generates numbers from the start value (0) up to but not including the stop value (10)


#here the loop got starting value 5 and the stop value is given by the parameter "end"
def print_numbers_from_five_to(end):
    for f in range(5, end):
        print(f)


#for the thired parameter of the range function, we can specify the step value, which determines how much the loop variable will be incremented in each iteration. By default, the step value is 1, but we can change it to any other value.def count_down(start, end):
    for i in range(start, end, -1):
        print(i)
#how the code will work: the start point is 10 and the end point is 5, now here where the step comes in, do i wanna coiunt down or count up on that i will put -1 as the step value, so the loop will decrement the value of i by 1 in each iteration,
#and it will print the numbers from 10 down to 6 (because the stop value is not included in the range).


#while loops are used when we want to repeat a block of code as long as a certain condition is true. The syntax for a while loop is:
def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health +=1
        enemy_distance -=2
    return current_health
#in this example, the while loop will continue to execute as long as the current health is less than the maximum health and the enemy distance is greater than 3.
#Inside the loop, we are incrementing the current health by 1 and decrementing the enemy distance by 2 in each iteration. Once either of the conditions becomes false,
#the loop will stop executing and the function will return the current health.


#Continue Statement: means "go directly to the next iteration of this loop." Whatever else was supposed to happen in the current iteration is skipped.
def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter += 1
        if counter < 3:
                continue
        else:
            counter = 0
        enchantment_strength = quest_number * 5
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )


#plus it can help avoiding unnecessary work, like calculating square roots, we might want to skip negative numbers.
#continue lets us move on to the next number without wasting any time:
for number in range(-5, 5):
    if number < 0:
        continue  # Skip negatives

    print(f"The square root of {number} is {number ** 0.5}")