l1 = [1,2,3,4,5,6]# homogeneous list
print(l1,type(l1))
l2 = [1,2.5,'shilpa',True,5j]  # Heterogeneous list
print(l2,type(l2))
print()

print("Length of the list::",len(l2)) # Length of list
print()

print('----------------list constructor()---------------------')
p = list(('a',4.3,7j,'Pranaya',False))
print("We can type case list as above:\n",p,type(p))
print()

print('----------------list accessing using loops---------------------')
for k in p:
    print(k)
print()

print('----------------Membership in lists---------------------')
print(p)
if "Pranaya" in p:
    print("Pranaya is in the list")
if 4 in p:
    print('Yes')
else:
    print("4 is Not in the list")
print()

print('----------------Changing the list items---------------------')
veg = ['cucumber','carrot','beetroot']  # replaces the item
print("Before changing: ",veg)
veg[0]='beans'
print("After changing: ",veg)
veg[0:2]=['Potato','Guava'] #changing range of items
print("After changing range of items: ",veg)
print()

print('----------------Insert items---------------------')
print(veg)
veg.insert(0,'Pineapple') # takes arguments as index & value
print("After inserting the value in first position:\n",veg)
print()

print('---------------Append list items---------------------')
print("Before appening::",veg) # Appends the data at the end of the list
veg.append(20)
print("After appending::",veg)
veg.append([3.5,'Mango'])  # It becomes nested list if we add list of items using append
print("After appending another list::",veg)
print()

print('---------------Extend list items---------------------')
fru = [20,10,30]
print("Before extending::",fru)
fru.extend([40,50])  # Extend function adds the list of items in same sequence
print("After extending::",fru)
fru.extend(l1)
print("After extending another list::",fru)
print()

print('---------------Remove items---------------------')
print("Before removing::",fru) # while using remove() function we must give a value
fru.remove(50)
print("After removing::",fru)
print()

print('---------------Remove specified index---------------------')
print("Before popping out::",veg)  # Pop removes the last value or (-1) index value
veg.pop()
print("After using pop function::",veg)
veg.pop(0)
print("After removing the specified item using index::",veg)
print()

print('---------------Emptying the list--------------------')
veg.clear()    # It prints the empty list
print(veg)  # if we use del keyword to del the list it prints nothing.
print()

print('---------------copying  the list--------------------')
new = [3,4,5,2]
cp=new.copy()
print("After copying the list::",cp)
print()

print('---------------Count in the list--------------------')
n = [1,1,1,2,2,3,1,4,5,6,3,2]
print("The count of 1 in the list is::",n.count(1))

