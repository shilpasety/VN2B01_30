amt = int(input("Enter amount:"))
if(amt>=0 and amt<=100):
    disc = amt*(5/100)
    net = int(amt-disc)
    print("After Discount you should pay",net,"/-")
elif(amt>=101 and amt<=200):
    disc = amt * (10 / 100)
    net = int(amt - disc)
    print("After Discount you should pay", net, "/-")
elif(amt>=201 and amt<=300):
    disc = amt * (15 / 100)
    net = int(amt - disc)
    print("After Discount you should pay", net, "/-")
elif(amt>300):
    disc = amt * (22 / 100)
    net = int(amt - disc)
    print("you should pay", net, "/-")
else:
    print("Please purchase something")