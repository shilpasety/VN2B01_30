mrp = int(input("Enter the amount:"))
if(mrp>10000):
    net = int(mrp-(0.2*mrp))
    print("Pay",net,"after Discount")
elif(mrp>7000 and mrp<=10000):
    net = int(mrp-(0.15*mrp))
    print("Pay", net, "after Discount")
elif(mrp<=7000 and mrp>0):
    net = int(mrp - (0.1 * mrp))
    print("Pay", net, "after Discount")
else:
    print("Sorry. No Discount")
