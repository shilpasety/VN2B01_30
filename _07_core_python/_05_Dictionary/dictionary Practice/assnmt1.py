'''Merging 2 dictionaries into 1'''
d1 = {1:'Shilpa',2:'Asha',3:'Advaitha'}
d2 = {4:'Pranaya',5:'Rama'}
d1.update(d2)
print(d1)
print(d2)

''' Taking User input and mapping it into Dictionary'''
x = int(input("Enter the size:"))
l=[]
p=[]
print("Enter the keys::")
for i in range(x):
  k = int(input())
  l.append(k)
print("Enter the values")
for j in range(x):
  v = str(input())
  p.append(v)

d = dict(zip(l,p))
print("The Dictionary:",d)

'''second method to take user input using update method'''

print()
d={}
y = int(input("Enter the size:"))
print("Enter the keys & values::")
for i in range(y):
  k = int(input())
  v= input()
  d.update({k:'v'})
print("The dictionary is::",d)