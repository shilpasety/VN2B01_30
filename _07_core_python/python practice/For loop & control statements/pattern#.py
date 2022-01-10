print("-----------Using for loop-------------")
for i in range(4):
    for j in range(4):
        print('#',end='')
    print()
print()
print("-----------Using while loop-------------")
i=1
while(i<=4):
    j = 1
    while(j<=4):
        print('#',end=' ')
        j+=1
    print()
    i+=1