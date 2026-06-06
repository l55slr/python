#A "for loop" in Python is written like this:
for i in range(0, 10):
    print(i)
#this will print the numbers from 0-9 because the range function generates numbers from the start value (0) up to but not including the stop value (10)


#here the loop got starting value 5 and the stop value is given by the parameter "end"
def print_numbers_from_five_to(end):
    for f in range(5, end):
        print(f)