print("Even or odd program\n")
a=int(input("Enter a num: ")) #By default user input is string,so give the required format

if (a%2==0):
    print("Even")
    if(a>10):    #Nested if
        print("Greater than 10")
    else:
         print("Smaller than 10")
else:
    print("Odd")





