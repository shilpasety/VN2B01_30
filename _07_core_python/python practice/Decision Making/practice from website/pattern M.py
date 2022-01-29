'''Write a Python program to print alphabet pattern 'M'. Go to the editor
Expected Output:

  *       *
  *       *
  * *   * *
  *   *   *
  *       *
  *       *
  *       *'''
for i in range(2):
    for j in range(2):
        print('*',end='         ')
    print()
print('*  *   *  *')
print('*    *    *')
for i in range(3):
    for j in range(2):
        print('*',end='         ')
    print()