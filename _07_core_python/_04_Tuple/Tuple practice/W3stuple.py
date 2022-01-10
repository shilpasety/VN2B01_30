tup = tuple((1,2,3,4,5))
print(tup[-4:-1])

print('-----------------Change Tuple values---------------------------')
l = list(tup)  #As tuples are immutable we can't directly change them, convert them
print(type(l))
l[0:2]=['Pranaya',['a','b']]
tup=tuple(l)
print(tup,type(tup))
print()

print('-----------------Adding tuple to a tuple---------------------------')
t1 = (1,2,3)  # We can concatenate tuples using + symbol. we can extend the tuple using + symbol
t2 = ('a','b','c')
t1 =t1+t2
print(t1)
print()

print('-----------------Remove tuple items---------------------------')
l = list(t1)
print("Before removing::",t1)
l.pop(3)
t1 = tuple(l)
print("After removing 'a'::",t1)
print()

print('-----------------Deleting the tuple--------------------------')
del t2
#print(t2)   # raises an error as it is already deleted
print()

print('-----------------Looping through tuple--------------------------')
print(t1)
i=0
while i<len(t1):
    print(t1[i])
    i=i+1
print()

print('----------------Multiplying the tuple--------------------------')
print("After multiplying the tuple with 3::\n")
t1=3*t1
print(t1)
print()

print('-----------------Buil in methods--------------------------')
c= (10,10,20,30,40,10,20)
print(c)
print("count the occurences of 10::",c.count(10))
print()

print('-----------------Index--------------------------')
print("The index value of 10::",c.index(10)) # it gives the index of first occurence
print()

print('-----------------Max and min elements--------------------------')
print(c)
print("The maximun element::",max(c))
print("The minimun element::",min(c))