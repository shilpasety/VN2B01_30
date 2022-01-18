'''Write a Python program to print alphabet pattern 'D'. Go to the editor
Expected Output:

 ****
 *   *
 *   *
 *   *
 *   *
 *   *
 **** '''

print('*'*4,end='')
print()
for i in range(5):
    for j in range(2):
        print('*',end='   ')
    print()
print('*'*4,end='')