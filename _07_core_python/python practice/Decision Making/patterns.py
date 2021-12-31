'''
printing the pattern in ascending order
'''
print("******Ascending order printing****")
x=int(input("Enter a number:"))
for i in range(1,x+1):
    for j in range(i):
        print("$",end=' ')
    print()
print('-------------------------')
'''
printing the pattern in descening order
'''
print("*******Printing the pattern in Descending order********")
y= int(input("Enter a number:"))
for i in range(y,0,-1):
    for j in range(i):
        print("*", end=' ')
    print()