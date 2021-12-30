x = int(input("Enter the number of sides:"))
if(x==3):
    print("Triangle",x,"sides")
elif x==4:
    print("Either Square or Rectangle",x,"sides")
elif(x==5):
    print("Pentagon",x,"sides")
elif(x==6):
    print("Hexagon",x,"sides")
elif(x==8):
    print("Octagon",x,"sides")
else:
    print("There is no shape with the given number")

