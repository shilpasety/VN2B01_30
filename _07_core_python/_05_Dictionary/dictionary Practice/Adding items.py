# We can add the items to dictionary in 2 ways:, by using a new index key and assigning value to it or
# updating the dictionary
'''Note: We can use update in 2 ways:
1-to update the already existing value using the same key
2-to update the dictionary by adding new key-value pair'''
d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Before adding:",d)
d['color']='red'
print("After adding:",d)
print()
print('------------------------Updating dictionary---------------------------')
print("Before updating:",d)
d.update({'owner':'Advaitha'})
print("After updating:",d)