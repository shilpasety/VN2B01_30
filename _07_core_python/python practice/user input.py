'''
Instead of directly assigning the value, we are asking the user to manually enter it

.
'''

x= int(input("Enter a value:"))    #By default input function takes input in string format. So we should
# mention the required format
v=int(input("Enter another value:"))
print("Addition",x+v)
print("Multiplication",x*v)
print("Exponential",x**v)

a=float(input("To which num you want square?"))
print(a**2)

import math as m
b= int(input("Factorial of"))
print(m.factorial(b))

'''
Find the cube of a number & take input from user
'''

cube = int(input("Cube of: "))
print(cube*cube*cube)
print(m.pow(cube,3))   # By default math function returns float value
