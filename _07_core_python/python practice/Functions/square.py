'''Write a Python function to create and print a list where the values are square of numbers
between 1 and 30 (both included)'''

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,4,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
s=[] # since it's global we can use anywhere in the program
def squares(sq):
    for i in sq:
        s.append(i**2)
    return s

print("The squares list:\n",squares(l))