#Comparison Operators
"""
< "less than"
> "greater than"
<= "less than or equal to"
>= "greater than or equal to"
== "equal to"
!= "not equal to"
"""
#If Statements
if 2 > 1:
    print("2 is greater than 1")


#If-Else Statements
if 2 < 1:
    print("2 is less than 1")
else:
    print("2 is not less than 1")


#elif Statements
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")