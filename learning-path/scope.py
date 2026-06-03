#1. will define a function that subtracts two numbers and then tries to print the value of x outside the function.
#that will not work cuz X is not a globle scope, that means it only exists inside the function, and we can't access it outside the function.
def subtract(x, y):
      return x - y
result = subtract(5, 3)
#print(x)
# ERROR! "name 'x' is not defined"

#2. but what if the C is a global scope, then we can access it outside the function.
c = 10
def add(a, b):
      return a + b + c
result = add(5, 3)
print(result) # this will print 18 because c is a global variable and we can access it inside the function.
print(c)