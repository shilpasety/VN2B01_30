lis = [2,'Banana',3.5,'Carrot',4+6j,True,False,4+6j]
print(len(lis))
print(lis[0:3])
print(type(lis))
print(id(lis),id(lis[0]),id(lis[4]),id(lis[7]))

dup = lis
print(id(dup))

lis1 = [2,'Banana',3.5,'Carrot',4+6j,True,False,4+6j]
print(id(lis1))

cast = list((2,4,'Jerry'))
print(cast)

print ('------------------------')

print("*********Changing the list items**********\n")

aca = ["apple", "banana", "cherry","Watermelon"]
print(aca)
aca[1]='beetroot'      # Since lists are mutable, I can change it's contents
print(aca)

print ('------------------------')
print("*******Changing the range of items**********\n")

aca = ["apple", "banana", "cherry","Watermelon"]
print(aca)
aca[0:2]= ['Pranaya','Advaitha',35,87]
print(aca)

aca[0:2]=['sudha']
print(aca)

print ('------------------------')
print("******Inserting new items******\n")

lis = [2,'orange',(23,12,'kiwi'),{1,1,2,1,2,3}]
lis1 = ['Om','Siva']
lis2 =lis+lis1
print(lis2)