print('-----------1.Built-in function approach-------------------')
print()

txt = input('Enter string:')
l=len(txt)
x=txt[0].swapcase()
y=txt[len(txt)-1].swapcase()
print(x+txt[1:l-1]+y)

print()

print('-----------2.Algorithm approach-------------------')
print()

s = input('Enter string:')
l=len(s)
for i in range(l):
    x=s[0].swapcase()
    y=s[l-1].swapcase()
    break
print(x+s[1:l-1]+y)

print()

print('-----------3.Function approach-------------------')
print()

s = input('Enter string:')
l=len(s)

def up_low_swap(n):
    for i in range(l):
        x=n[0].swapcase()
        y=n[l-1].swapcase()
        break

up_low_swap(s)
print(x+s[1:l-1]+y)

print()

print('-----------4.OOPS approach-------------------')
print()

class Fir_last:

    l=len(s)  #class variable

    def __init__(self):
        self.s = input('Enter string:')  #instance variable 

    def flswap(self):   #instance method can use both instance variables and class variables
        for i in range(l):
            x = self.s[0].swapcase()
            y = self.s[l - 1].swapcase()
            break
p1 = Fir_last()
p1.flswap()
print(x+s[1:l-1]+y)
