'''a=int(input("Enter a num: ")) #By default user input is string,so give the required format

if (a%2==0):
    print("Even")
    if(a>10):    #Nested if
        print("Greater than 10")
    else:
         print("Smaller")
else:
    print("Odd") '''



'''p= int(input("Enter a number: "))
if(p>0):
    print("positive number")
else:
    print("Negative number") '''

r = int(input("first number: "))
n = int(input("Second number: "))
y=  int(input("Third number: "))

if(r>n and r>y):
    print("First number",r)
elif(n>r and n>y):
    print("Second number",n)
else:
    print("Third number",y)