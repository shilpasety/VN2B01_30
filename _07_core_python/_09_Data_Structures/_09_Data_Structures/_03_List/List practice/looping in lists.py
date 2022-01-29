print('---------------Using for loop------------------')
g= ['apple','banana','cherry'] #printing the order in reverse using for loop
for i in range(len(g)-1,-1,-1):  #looping through their index values
    print(g[i])

print()
print("-------------------Using while loop------------------------")
i=0
while(i<len(g)):
    print(g[i])
    i=i+1
print()

print("-------------------Sorting the list------------------------")
h= [34,23,56,12,78]
print("Before sorting::",h)
h.sort()
print("After sorting in Ascending order::",h)
h.sort(reverse=True)
print("After sorting in descending order::",h)
r= ['Home','alas','Goat','Zebra','boom']
print("Before sorting::",r)  #by default lists sorting is case sensitive
r.sort()
print("After sorting::",r)
r.sort(key=str.lower) # by using str.lower method we can get the case-insensitive sorting
print("After sorting::",r)