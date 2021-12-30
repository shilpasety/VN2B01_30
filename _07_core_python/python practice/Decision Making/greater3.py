r = int(input("first number: "))
n = int(input("Second number: "))
y=  int(input("Third number: "))

if(r>n and r>y):
    print(r,">",n,"&",y)
elif(n>r and n>y):
    print(n,">",r,"&",y)
else:
    print(y,">",r,"&",n)