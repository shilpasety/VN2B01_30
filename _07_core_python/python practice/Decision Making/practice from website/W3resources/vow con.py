'''Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k
k is a consonant.'''

c = input("Enter a character:")
if c.lower()=='a' or c.lower()=='e' or c.lower()=='i' or c.lower()=='o' or c.lower()=='u':
    print(c,"is a vowel")
else:
    print(c, "is a consonant")

