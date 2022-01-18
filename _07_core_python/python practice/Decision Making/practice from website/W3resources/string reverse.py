'''Write a Python program that accepts a word from the user and reverse it'''
s = input("Enter a word:")
l=len(s)
print("The reversed string:")
for i in range(l-1,-1,-1):
    print(s[i],end='')

