print('-----------1.Built-in function approach-------------------')
print()
st = input('Enter string:')
print(st[0:2])

print('-----------2.Algorithm approach-------------------')
print()

st = input('Enter string:')
a = int(input('Start index:'))
b = int(input('End index:'))
for i in range(len(st)):
    print(st[a:b])
    break

print()

print('-----------3.Function approach-------------------')
print()
st = input('Enter string:')

def Slice(qw):
    a = int(input('Start index:'))
    b = int(input('End index:'))
    for i in range(len(st)):
        print(st[a:b])
        break
Slice(st)

print()

print('-----------4.OOPS approach-------------------')
print()

class Slice:
    def __init__(self):
        self.st = input('Enter string:')
    def slic(self):
        a = int(input('Start index:'))
        b = int(input('End index:'))
        for i in range(len(self.st)):
            print(self.st[a:b])
            break
p1 = Slice()
p1.slic()

