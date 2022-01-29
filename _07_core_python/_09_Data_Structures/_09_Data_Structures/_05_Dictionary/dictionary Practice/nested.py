print('--------------Nested dictionary----------------------')
family = dict({
    'child1':{'name':'Advaitha','year':2015},
    'child2':{'name':'Pranaya','year':2018},
    'child3':{'name':'Minnu','year':2020}
})
print(family)
print("Accessing values:",family['child1']['name'])
print()
# Or we can create dictionaries seperately, create other dictionary that will contain all the other dictioanries
child1 = {'name':'Advaitha','year':2015}
child2 = {'name':'Pranaya','year':2018}
child3 = {'name':'Minnu','year':2020}
family ={
    'child1':child1,
    'child2':child2,
    'child3':child3
}
print(family)

print()
print('-----------------------fromkeys method------------------------------')
x= ('a','b','c')

d = dict.fromkeys(x)
print(d)