print("Select Operation")
print("1.Add\n2.Substract\n3.Multiply\n4.Divide")
x= int(input("Enter choice(1/2/3/4):"))
while x<=4:
    a= int(input("Enter first number:"))
    b= int(input("Enter second number:"))
    if x==1:
        c=a+b
        print(a,"+",b,"=",c)
        break
    elif x==2:
        c=a-b
        print(a,"-",b,"=",c)
        break
    elif x==3:
        c=a*b
        print(a,"X",b,"=",c)
        break
    elif x==4:
        c=a/b
        print(a,"/",b,"=",c)
        break
if x>=5:
    print("Sorry!")




