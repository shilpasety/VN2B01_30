'''Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("The list is:",l)
print()
e=[]  #global scope
def leven(l):
    for i in l:
        if i%2==0:
            e.append(i) #using global variable inside a function
    return e
print("Only even numbers list:\n",leven(l))