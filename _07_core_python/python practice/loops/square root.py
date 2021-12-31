'''
Finding the square root of given number
'''
import math
x = int(input("Enter a number:"))
s=math.sqrt(x)
if(s%1==0):
    print(x,"is a perfect square num & it's root is:",int(s))
else:
    print(x,"is not a perfect square")


print('--------------------------------')

'''
Find the square root numbers in the given range
'''
print("perfect squares from 1 to 50")
c=0
for i in range(1,50):
    s=pow(i,0.5)
    if(s%1==0):
        print(i)
        c+=1
print("count=",c)
print('------------------------------------------------')
print("Printing the perfect squares from the given range")
c=0
a=int(input("Enter a num:"))
b=int(input("Enter a num:"))
for i in range(a,b):
    s = pow(i, 0.5)
    if (s % 1 == 0):
        print(i)
        c += 1
print("count=", c)