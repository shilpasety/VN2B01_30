print('-----------1.Built-in approach-------------------')
print()

s = input('Enter longest string:')
l=[]
p = s.split()
for i in p:
    c=len(i)
    l.append(c)
print(max(l))

print()

print('-----------2.Algorithm approach-------------------')
print()

s = input('Enter longest string:')
l = s.split()
p=[]
for i in l:
    c=0
    for j in i:
        c+=1
    p.append(c)
max = p[0]
for i in p:
    if i>max:
        max = i
print(max)

print()

print('-----------3.Function approach-------------------')
print()

s = input('Enter longest string:')
l=[]
def longest(ln):
    p=ln.split()
    for i in p:
        c = len(i)
        l.append(c)

    max = l[0]
    for k in l:
        if k>max:
            max=k
    return max

print(longest(s))

print()

print('-----------4.OOPS approach-------------------')
print()

class Longes:

    l=[]

    def __init__(self):
        self.s = input('Enter longest string:')
    def longest(self):
        p = self.s.split()
        for i in p:
            c = len(i)
            l.append(c)

        max = l[0]
        for k in l:
            if k > max:
                max = k
        return max

p1 = Longes()
print(p1.longest())



