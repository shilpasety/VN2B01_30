'''Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''
print("------------User defined List-----------------")
l=[]
z = int(input("Enter the size:"))
print("Enter the values:")
for i in range(z):
    x= int(input())
    l.append(x)

print(l)
def lsum(a):
    sum=0
    for i in l:
        sum = sum+i
    print("Total sum:",sum)

lsum(l)
print()

print('-------------------Defined list------------------------')
print()
lst=  [8,2,3,0,7]
print(lst)
def lst_sum(lst1):
    sum=0
    for j in lst1:
     sum=sum+j
    print("Total sum:",sum)
lst_sum(lst)
