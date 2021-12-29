amt = int(input("Enter the amount:"))
if(amt>=6000 and amt<7000):
    print("You're allotted to 3-sharing")
elif(amt>=7000 and amt<10000):
    print("You're allotted to 2-sharing")
elif(amt>=10000 and amt<=12000):
    print("You're allotted to 1-sharing")
else:
    print("we have no rooms for the entered amount")