print ("How elif works\n")
a= 'Goal'
b= 'Success'
c= 'Goal'
if a==b or b==c:
    print("Not at all")
elif a==b or a==c:
    print("Just checking the elif work")
elif a==c or a==b:
    print("Yeah, Goal & Goal are equal")
else:
    print("All the above are false")
