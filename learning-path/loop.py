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