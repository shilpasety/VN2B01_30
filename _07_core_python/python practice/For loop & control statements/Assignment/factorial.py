print("Factorial of a given num using import math function")
import math
a= int(input("Enter a number:"))
print("Factorial of",a,"is:",math.factorial(a))

print('------------------------')
print("Factorial of a given num using for loop")
fact =1
a= int(input("Enter a number:"))
for j in range(a,1,-1):
    fact = fact*j
print("Factorial of",a,"is:",fact)