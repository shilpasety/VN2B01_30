print('Printing a complex number')
x= 3+4j
print(x,type(x))

print('-----------------')

print('finding the type as list')
y= ['Advaitha',30,2.5,4+6j]
print(y,type(y))
print(y[1])
y[1]=45
print(y)

Y= list((20,40,'Adorable',67.8))
print(Y,type(Y))

print('----------------')

print('Finding the type as Tuple')
z=(20,'Challenge',40.5,4+5j)
print(z,type(z))

Z= tuple((2,3,1,'Success'))
print(Z,type(Z))

print ('----------------')

print ('Range')
c= range(5)
print(c[4],type(c))

print ('----------------')

print('Mapping type: Dictionary')

d= {'Java':'VSC','Python':'Pycharm'}
print(d,type(d))
D = dict(name='Python',age=45)
print(D,type(D))

print('--------------------------')

print('Set')
s = {34,45,23,67}
print(s,type(s))

print('----------------------')
print('Boolean type')
b= True
B = bool(6.7)
print(b,type(b))
print(B,type(B))
z= bool(0)
print(z,type(z))