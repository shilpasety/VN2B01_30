'''Write a Python program to print alphabet pattern 'R'. Go to the editor
Expected Output:

 ****
 *   *
 *   *
 ****
 * *
 *  *
 *   *'''
for i in range(4):
    print('*',end='')
print()
for i in range(2):
    for j in range(5):
        if j==0 or j==4:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(4):
    print('*',end='')
print()
print('* *')
print('*  *')
print('*   *')