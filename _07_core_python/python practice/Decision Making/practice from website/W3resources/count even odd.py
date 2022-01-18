'''Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4'''

l=[]
s = int(input("Enter the size:"))
print("Enter values:")
for i in range(s):
    x = int(input())
    l.append(x)
print("Numbers=",l)
c=0
d=0
for i in l:
    if i%2==0:
        c=c+1
    else:
        d=d+1
print("Number of even numbers:",c)
print("Number of odd numbers:",d)