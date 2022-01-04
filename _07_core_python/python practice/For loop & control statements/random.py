sq = [1,2,3,4,5]
for i in sq:
   print("Square of",i,"is:",i**2)

print('--------------------------------------')

#Print  first 4 numbers  which are divisible by 9 between 1 to 100
count=0
for x in range(1,101):
   if x%9==0:
      print(x)
      count+=1
      if count==4:
         break
print("Since it is not following the indentation :Out of the loop")
print('--------------------------------------')
#Print first 7 even numbers between 1 to 100
count=0
for i in range(1,100):
   if i%2==0:
      print(i)
      count+=1
      if count==7:
         break
print("Hurray, Out of the loop")
print('--------------------------------------')
#REQ: Find first 3 numbers which are divisible by 3 between 500 to 1000
count=0
for x in range(500,1000):
   if x%3==0:
      print(x)
      count+=1
      if count==3:
         break
print('--------------------------------------')
# Numbers between 1 to 1000 which are divisible by 5.
      # If value is also divisible by 10 don't display it.


