'''Write a Python program to print alphabet pattern 'O'. Go to the editor
Expected Output:

  ***
 *   *
 *   *
 *   *
 *   *
 *   *
  *** '''
print(' *** ')
for i in range(5):
    for j in range(2):
        print('*',end='   ')
    print()
print(' *** ')