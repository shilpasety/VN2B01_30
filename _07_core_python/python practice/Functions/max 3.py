'''Write a Python function to find the Max of three numbers'''
def max(x,y,z):
    if x>y and x>z:
        print(x,">",y,",",z)
    elif y>x and y>z:
        print(y,">",x,",",z)
    else:
        print(z,">",x,",",y)
max(56,45,78)

def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
wow = max3(23,12,10)
print(wow)

