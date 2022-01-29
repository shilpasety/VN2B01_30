'''Write a Python program to print alphabet pattern 'G'. Go to the editor
Expected Output:

  ***
 *   *
 *
 * ***
 *   *
 *   *
  *** '''

for k in range(4):
    if k==1 or k==2 or k==3:
        print('*',end='')
    else:
        print(' ',end='')
print()
for j in range(5):
    if j==0 or j==4:
        print('*',end='')
    else:
        print(' ',end='')
print()
for k in range(1):
    print('*')
for i in range(5):
    if i==0 or i==2 or i==3 or i==4:
        print('*',end='')
    else:
        print(' ',end='')
print()
for i in range(2):
    for j in range(5):
        if j == 0 or j == 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for k in range(4):
    if k==1 or k==2 or k==3:
        print('*',end='')
    else:
        print(' ',end='')

