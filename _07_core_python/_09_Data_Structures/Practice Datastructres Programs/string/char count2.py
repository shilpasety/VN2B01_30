


print('-----------2.Algorithm approach-------------------')
print()

a = input('Enter string:')
c=0
l=['0','1','2','3','4','5','6','7','8','9']
for i in a:
    if i!=' ' and i not in l:
        c+=1
print('Characters count is:',c)

print()

print('-----------3.Function approach-------------------')
print()

a = input('Enter string:')
def char_count(b):
    c=0
    for j in range(len(b)):
        if b[j]!=' ':
            c+=1
    return c
res = char_count(a)
print('Characters count is:',res)

'''I'm unable to use global variable inside function'''
