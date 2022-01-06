n= int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum = sum+i
    print(i,"+",end='')
print()
print("The sum of given natural numbers:",sum)