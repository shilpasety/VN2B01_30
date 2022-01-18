'''Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument'''

def fact(q):
    m=1
    if q==0:
        return 1
    else:
        for j in range(n,0,-1):
            m=m*j
        return m
n= int(input("Enter a number:"))
print("The factorial of",n,"is:",fact(n))

