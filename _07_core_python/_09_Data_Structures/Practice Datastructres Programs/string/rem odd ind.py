'''Remove odd index values in a string'''

print('-----------1.Built-in approach & Algorithm approach-------------------')
print()

s = input('Enter string:')
for i in range(len(s)):
    if i%2==0:
        print(s[i], end=' ')

print()

print('-----------3.Functions approach-------------------')
print()

s = input('Enter string:')

def rem_odd(st):
    for i in range(len(st)):
        if i%2==0:
            print(st[i],end=' ')

rem_odd(s)

print()

print('-----------4.OOPS approach-------------------')
print()

class Remove:

    def __init__(self,st):
        self.st = st

    def oddindex(self):
        for i in range(len(self.st)):
            if i % 2 == 0:
                print(self.st[i], end=' ')

ob = Remove('India needs more strong women')
ob.oddindex()
