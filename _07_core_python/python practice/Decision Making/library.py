days = int(input("Enter the number of Days:"))
if (days<=5 and days>=0):
    charge = 2*days
    print("Pay",charge,"/-")
elif(days>=6 and days<=10):
    charge = 3 * days
    print("Pay", charge, "/-")
elif(days>=11 and days<=15):
    charge = 4 * days
    print("Pay", charge, "/-")
else:
    charge = 5 * days
    print("Pay", charge, "/-")