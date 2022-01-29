print('-----------2.Algorithm approach-------------------')
print()

s = input('Enter string:')
l = len(s)
li=[]
for i in s:
    li.append(i)
for i in range(l):
    li[0],li[l-1]=li[l-1],li[0]
    break
print(''.join(li))

print()






