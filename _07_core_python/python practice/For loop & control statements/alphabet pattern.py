a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
print(len(a))
for q in range(1,len(a)):
    for j in range(q):
        print(a[q],end=' ')
    print()
