d = {1:'Shilpa',2:'Asha',3:'Pranaya',4:'Shilpa'}
print(d)
print(d[1])
print(d.keys())
print(d.values())
print(d.items())
d[4]='Advaitha'
print(d)

print('-------------------Dictionary items-------------------------')
d = {'brand':'ford','model1':'mustang','year':1964,'year':1920} #It is wrong to repeat the same key name, it doesn't throw error instead it overwrites the previous value
print(d['brand'])
print(d.get('brand')) #Another method to access value
print(d,type(d))
print('-------------------checking if key exists-------------------------')
if 'model1' in d:
    print("Yes, this key is present")
print()
print('-------------------Change values-------------------------')
print("Before changing",d)
d['year']=2018
print("After changing",d)
print()
print('-------------------Using update method------------------------')
print("Before updating:",d) # We can update the vlaues using update method
d.update({'year':2022})
print("After updating:",d)

print()
print("------------------Using get method----------------------------")
print(d)
print(d.get('mustang')) # we must give argument as key name--it fetches the value