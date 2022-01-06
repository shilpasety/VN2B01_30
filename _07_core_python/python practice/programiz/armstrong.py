'''
Write a program to check whether the given number is Armstrong or not?
Armstrong = it's digits cubes sum = the given number
'''
arm = input("Enter the number:") #1634
l= len(arm)
sum=0
for i in arm:
    sum = sum+int(i)**l
if sum==int(arm):
    print(arm,"is Armstrong number")
else:
    print(arm,"is not Armstrong number")