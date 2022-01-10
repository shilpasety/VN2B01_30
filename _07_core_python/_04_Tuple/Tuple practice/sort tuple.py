t = ([7, 5, 4], [8, 2, 4], [0, 7, 5])
l =list(t)
print(l)
l1=[]
for i in range(len(t)):
    l[i].sort()
    l1.append(l[i])
t=tuple(l1)
print("After sorting the tuple::",t)

