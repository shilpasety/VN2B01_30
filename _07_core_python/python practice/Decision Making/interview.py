x= int(input("Enter the no.of units:"))
if(x<=100):
    print("No charge")
elif(x>100 and x<=200):
    ch = (x-100)*5
    print("Please pay",ch,"/-")
elif(x>200):
    ch = x-200
    ch1 = (ch*10)+500
    print("Please pay",ch1,"/-")
else:
    print("Enter valid value")
