print("The available categories are:\n")
print("1.Commercial\n2.Institutional\n3.Domestic")
cat = input("Enter your category type:")
if(cat=='commercial'):
    u = int(input("Enter no.of units:"))
    if(0>u<=5000):
        print("The bill is 1500/-")
    elif(10000<=u>5000):
        b = 0.25*u
        sum = 1500+b
        print("The bill is",sum,"/-")
    elif(20000<u>10000):
        b = 0.23*u
        sum = 1500 + b
        print("The bill is", sum, "/-")
    else:
        b = 0.2 * u
        sum = 1500 + b
        print("The bill is", sum, "/-")
elif(cat=='institutional'):
    u = int(input("Enter no.of units:"))
    if (0 > u <= 5000):
        print("The bill is 1800/-")
    elif (10000 <= u > 5000):
        b = 0.3 * u
        sum=1800+b
        print("The bill is", sum, "/-")
    elif (20000 < u > 10000):
        b = 0.28 * u
        sum = 1800 + b
        print("The bill is", sum, "/-")
    else:
        b = 0.25 * u
        sum = 1800 + b
        print("The bill is", sum, "/-")
elif(cat=='domestic'):
    u = int(input("Enter no.of units:"))
    if (0 > u <= 100):
        print("The bill is 75/-")
    elif (200 <= u > 100):
        b = 1.25 * u
        sum=75+b
        print("The bill is", sum, "/-")
    elif (400 < u > 200):
        b = 2 * u
        sum = 75 + b
        print("The bill is", sum, "/-")
    else:
        b = 2.5 * u
        sum = 75 + b
        print("The bill is", sum, "/-")
else:
    print("Sorry, we have no such category")
