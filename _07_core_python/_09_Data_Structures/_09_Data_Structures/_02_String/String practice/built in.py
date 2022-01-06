bn="Accident Prone Zone"

print(bn.capitalize())
print(bn.casefold())
print(bn.lower())
print(bn.center(30,"*"))
print(bn.count('e'))
print(bn.encode())
print(bn.endswith("Zone"))

print(" --------find() function-----------")
print(bn.find('z'))  # returns -1 if not found

print(" --------Index() function-----------")
print("The value found at",bn.index('A'))   # Used to find the index value of that particular value..returns error if not found


tab = 'H\te\tl\tl\to'
print(tab)      # \t size is 4 (by default)
print(tab.expandtabs())  # expandtabs size is 8 (by default)
print(tab.expandtabs(8))


txt = "My name is {name}"
print(txt.format(name='shilpa'))

print(" --------isalnum() function-----------")
al = "123qwe"  # returns true if the string is combination of only alpha & numeric or only alpha or only num
print("The string contains only alphanumeric values so, ",al.isalnum())
al = "qwe_12&"
print("The string doesn't contain only alphanumeric values so, ",al.isalnum())
print()

print(" --------isalpha() function-----------")

ph = "asha123"
print("The string doesn't contain only alpha values so, ",ph.isalpha())
ph = 'beyond'
print("The string contains only alpha values so, ",ph.isalpha())
print()

print(" --------isidentifier() function-----------")
a="1wer"
print("As it is started with number,",a.isidentifier())
b='qwe_12'
print("It can contain _& after that numbers,",b.isidentifier())
print()

print(" --------islower() function-----------")
c= 'hello World'
print("Since it doesn't contain only small letters,",c.islower())
c= 'hello 123'  # It should contain only small letters, doesn't care if it has numbers or not
print("Since it contains only small letters,",c.islower())

print()

print(" --------isspace() function-----------") #returns true only if the string is only white spaces
sp = '       '
print("Since it contains only spaces",sp.isspace())
sp = '       4'
print("Since it contains something",sp.isspace())
print()

print(" --------ljust() function-----------")
b= 'banana'
print("I like",b.ljust(15),"alot")
print("I like",b.ljust(15,'1'),"alot")
print()

print(" --------zfill() function-----------")
a= "kala"
print(a.zfill(10))
b="Guesswhat"
print(b.zfill(15))
c= 'Welcome to the world'
print(c.zfill(10)) # not filled with zeros as the string length is already exceeding the length given
print()

