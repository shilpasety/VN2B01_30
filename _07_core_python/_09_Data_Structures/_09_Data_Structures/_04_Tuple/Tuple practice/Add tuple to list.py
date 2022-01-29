y = int(input("Enter the size(list)::"))
l = []
print("Enter values into list:")
for i in range(y):
    p = int(input())
    l.append(p)
print(l)
d=[]
z = int(input("Enter the size(tuple)::"))
print("Enter values into tuple:")
for i in range(z):
    p = int(input())
    d.append(p)
tup = tuple(d)
print(tup)
print("Adding list to tuple:\n")
for q in range(z):
    l.append(tup[q])
print(l)
