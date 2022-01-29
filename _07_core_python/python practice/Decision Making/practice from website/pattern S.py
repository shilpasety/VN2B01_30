'''Write a Python program to print the following patterns. Go to the editor
Expected Output:

  ****
 *
 *
  ***
     *
     *
 **** '''
for i in range(5):
    if i==1 or i==2 or i==3 or i==4:
        print('*',end='')
    else:
        print(' ',end='')
print()
for i in range(2):
    print('*')
print(' ***')
for i in range(2):
    for j in range(5):
        if j==4:
            print('*',end='')
        else:
            print(' ',end='')
    print()
print('****')
