c = int(input("Enter the cost price:"))
if c>100000:
    t = 0.15*c
    print("Pay",t,"as tax")
elif c>50000 and c<=100000:
    t = 0.1*c
    print("Pay", t, "as tax")
elif c<=50000:
    t = 0.05*c
    print("Pay", t, "as tax")
else:
    print("Enter valid cost price")