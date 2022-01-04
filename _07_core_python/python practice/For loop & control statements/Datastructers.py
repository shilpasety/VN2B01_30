print("******List******")
li = list((2.3,'Goal',12,True,4j))
print(li,type(li))
for i in li:
    print(i)
print('-------------------------------')
print("******Tuple******")
tu = tuple((2.3,'Goal',12,True,4j))
print(tu,type(tu))
for i in tu:
    print(i)
print('-------------------------------')
print("******Dictionary******")
di =  dict({1:'Hello',2:'Hi',3:'Swagat'})
print("Keys:::::")
for i in di: #or for i in di.keys()
    print(i)
print("Values:::::")
for i in di.values():
    print(i)
print("Key,value pairs:::")
for i,j in di.items():
    print(i,j)

