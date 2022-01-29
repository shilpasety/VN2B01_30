print('--------------loop through dictionary--------------------')
d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('------------Keys-----------------------')
for i in d:  #returns only the keys
    print(i)
print()
print('------------values-----------------------')
for i in d:
    print(d[i])
print()
print('------------we can also use values method-----------------------')
for i in d.values():
    print(i)
print()
print('------------items-----------------------')
for u,v in d.items():
    print(u,v)
print()
print("--------Accessing as key value pair directly-----------")
for u in d.items():
    print(u)