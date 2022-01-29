'''Write a Python program that accepts a hyphen-separated sequence of words as input and prints the
words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''

st  = input('Enter hyphen seperated sequence of words:\n')
def sort_split(d):
    sp = d.split("-")
    print("-".join(sorted(sp)))

sort_split(st)

