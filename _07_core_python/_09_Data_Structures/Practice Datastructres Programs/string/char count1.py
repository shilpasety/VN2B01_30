print('-----------1.Built-in function approach-------------------')
print()

st = input('Enter string:')
c = input('Enter character for count:')
print(st.count(c))

print()

print('-----------2.Algorithm approach-------------------')
print()

st = input('Enter string:')
c = input('Enter character for count:')
co=0
for i in st:
    if i==c:
        co+=1
print(co)

print()

print('-----------3.Function approach-------------------')
print()

st = input('Enter string:')
def char_count(br):
    c = input('Enter character for count:')
    co = 0
    for i in br:
        if i == c:
            co += 1
    return co
print(char_count(st))

print()

print('-----------4.OOPS approach-------------------')
print()

class Char_count:
    def __init__(self):
        self.st = input("Enter string:")
    def myfunc(self):
        c = input('Enter character for count:')
        co = 0
        for i in self.st:
            if i==c:
                co+=1
        return co
p1 = Char_count()
print(p1.myfunc())
