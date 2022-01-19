'''Write a Python program to find the median'''
s = int(input('Enter the size:'))
print('Enter the values:')
l=[]
for i in range(s):
   x = int(input())
   l.append(x)
   if len(l)%2!=0:
       pass