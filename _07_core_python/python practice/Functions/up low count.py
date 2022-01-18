'''Write a Python function that accepts a string and calculate the number of upper case letters and
lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

s = input("Enter the string:")
def up_low_c(s):
    c=d=0
    for i in s:
        if i.isupper():
            c=c+1
        elif i.islower():
            d=d+1
    print("The no.of upper case characters:",c)
    print("The no.of lower case characters:", d)
up_low_c(s)


