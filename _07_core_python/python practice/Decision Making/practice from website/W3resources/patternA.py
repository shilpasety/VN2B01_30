'''Write a Python program to print alphabet pattern 'A'. Go to the editor
Expected Output:

  ***
 *   *
 *   *
 *****
 *   *
 *   *
 *   *'''
for u in range(4):
    if u==1 or u==2 or u==3:
        print('*',end='')
    else:
        print(' ',end='')
print()
for u in range(2):
    for k in range(2):
        print('*',end='   ')
    print()
for u in range(5):
    print('*',end='')
print()
for u in range(3):
    for k in range(2):
        print('*',end='   ')
    print()