'''Write a Python program to calculate the sum and average of n integer numbers
(input from the user). Input 0 to finish'''

n = int(input('Enter size:'))
l=[]
if n>=1:
    print('Enter values:')
    for i in range(n):
        x  = int(input())
        l.append(x)
    print(l)
    sum=0
    for j in l:
        sum = sum+j
    print('The sum:',sum)
    print('Average:',sum/len(l))

