u = int(input("Enter the no.of units:"))
if u>=0 and u<=100:
    print("No charge")
elif u>100 and u<=200:
    print("Total charge:",(u-100)*5)
elif u>200:
    b = u-100
    p = (b*10)-500
    print("Total charge:",p)
else:
    print("Enter valid number")