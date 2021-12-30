amt = int(input("Enter the amount:"))
if(amt>=1190):
    change = amt-1190
    if(amt==1190):
        print("Paid the exact amount for \"Deluxe pass\"")
    else:
        print("You get Change:",change,"& Deluxe pass")
elif(amt>=1090):
    change = amt-1090
    if(amt==1090):
        print("Paid the exact amount for \"Metro pass\"")
    else:
        print("You get change:",change,"& Metro pass")
elif(amt>=990):
    change = amt-990
    if(amt==990):
        print("piad the exact amount for \"Ordinary pass\"")
    else:
        print("You get change:",change,"& Ordinary pass")
else:
    print("Sorry, No passes available ")