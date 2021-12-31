'''
Factorial of a given num using import functions
'''
print("Using import math function")
import math
x= int(input("Enter a number:"))
print("The factorial of",x,"is=",math.factorial(x))


print('----------------------------------')
'''Basic method to calculate factorial of given number'''

print("Naive method to calculate factorial of a given number")
x = int(input("Enter a num:"))
fact=1
for i in range(1,x+1):
    fact = fact*i
print("The factorial of",x,"is=",fact)