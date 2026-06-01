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