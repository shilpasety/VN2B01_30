v = [20,10,5,12,5,80,8]
x=0
for i in v:
    x =i+x
print("Total sum:",x)
print('----------------------------')
print("*****Sum of numbers from 1 to 100*****")
sum=0
for i in range(1,101):
    sum = i+sum
print("Sum of 1 to 100 is",sum)
print('----------------------------')
print("*****Sum of numbers from 1 to 100(while loop)*****")
i=1
sum=0
while i<=100:
    sum = sum+i
    i+=1
print("Sum of 1 to 100 is",sum)