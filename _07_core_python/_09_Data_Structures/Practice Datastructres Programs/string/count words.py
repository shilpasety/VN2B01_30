'''Count words in a string'''

print('-----------1.Built-in approach approach-------------------')
print()

s  = input("Enter string:")
l=s.split()
print("Count of words in entered string::",len(l))

print()

print('-----------2.Algorithm approach-------------------')
print()

s  = input("Enter string:")
l=s.split()
c=0
for i in l:
    c=c+1
print("The count:",c)

print()

print('-----------3.Functions approach-------------------')
print()


def count():
    s = input("Enter string:")
    l = s.split()
    c = 0
    for i in l:
        c = c + 1
    return c


print(count())

print()

print('-----------4.OOPS approach-------------------')
print()

class Count:

    def __init__(self):
        self.s = input("Enter string:")

    def words(self):
        l = self.s.split()
        c = 0
        for i in l:
            c = c + 1
        return c

ob = Count()
print(ob.words())


