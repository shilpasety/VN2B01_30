x=int(input("Enter the tuple size:")) # took input from user
l = []
print("Enter the values into tuple::")
for i in range(x):
    a= int(input())
    l.append(a)
l1=[]
print("The cubes of tuple values::\n") # converted into list & again into tuple as their cubes
for j in range(x):
    b=l[j]**3
    l1.append(b)
print(tuple(l1))