print('-----------1.Built-in function approach-------------------')
print()

st = input('Enter string:')
print('Length of the string:',len(st))

print()

print('-----------2.Algorithm approach-------------------')
print()

st = input('Enter string:')
c=0
for i in st:
    c+=1
print('Length of the string:',c)

print()

print('-----------3.Function approach-------------------')
print()

st = input('Enter string:')
def length(r):
    c = 0
    for i in r:
        c+=1
    return c
print("The length of the string:",length(st))

print()

print('-----------4.OOPS approach-------------------')
print()

class Length:

    def __init__(self):
        self.st = input('Enter string:')

    def str_len(self):
        c=0
        for i in self.st:
            c+=1
        return c
p1  = Length()
print(p1.str_len())

