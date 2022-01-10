d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('-----------------------Using pop method-----------------------------')
print("Before removing:",d)
d.pop('brand')  # we must give 1 argument in pop (tell it what to remove exactly) by mentioning the key name
print("After removing:",d)
print()
d.update({'color':'red'})
print()
print('-----------------------Using popitem method-----------------------------')
print("Before removing:",d)
d.popitem() #removes the last pair in the dictionary
print("After removing the last item:",d)
print()
print('-----------------------Using del method-----------------------------')
d.update({'owner':'Shilpa'})
print("Before deleting:",d)
del d['year']
print("After deleting:",d)
print()
#Using del keyword we can also delete dictionary completely
dc = d.copy()
print("The copy of original dictionary",dc)
del dc
#print(d) ---raises an error not defined
print()
print('-----------------------Using clear method-----------------------------')
d.clear() #prints an empty dictionary
print("After clearing all the items:",d)