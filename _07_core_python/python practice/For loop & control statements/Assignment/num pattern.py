print("***Printing the number pattern***")
for k in range(1,5):
    for j in range(1,k+1):
        print(j,end=' ')
    print()

print('------------------------------')
print("***Printing the * pattern in reverse order***")

for m in range(4,0,-1):
    for l in range(m):
        print('*',end=" ")
    print()

print('---------------------------')

print("Printing the number pattern in reverse order")
for i in range(5,0,-1):
    for j in range(i):
            print(i,end=' ')
    print()