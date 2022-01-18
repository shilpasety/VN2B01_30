'''Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2'''
s = input("Enter the string:")
c=d=0
for i in s:
    if i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1
    else:
        pass
print("Letters:",c)
print("digits:",d)