print ("only if statement")
a = 33
b = 200
if a<b :
    print("33 is less than 200")

print('----------------')

print ("checking the elif conditions:\n")

c = 33
d = 33
if c<d:
    print("33 is less than 33")
elif c==d:
    print("c is equals to d here")

print('----------------')

print (" checking the else condition here(with elif present):\n")

e= 200
f= 33
if e<f:
    print("200 is less than 33")
elif e==f:
    print("200 and 33 are equal")
else:
    print("200 is greater than 33")

print('----------------')

print('else condition without elif:\n')
g = 'Challenge'
h = 'hardwork'

if(g==h):
    print ("Challenge and hardwork are equal")
else:
    print("Challenge & Hardwork are not the same")

print('----------------')

print ("Short hand if:\n")

a = 'Dedication'
b = 'Goal'
if (a!=b): print("Yeah")

print('----------------')

print ("Shorthand if ....else\n")
print ("Holds true") if (a==b) else print("Always Not the same ")

print('----------------')

print ("\"and\" keyword is used here\n")
a=200
b=33
c=500
if a>b and c>b:
    print("Both conditions satisfied\n")

print ("\"or\" keyword is used here\n")

if a<b or b<c:
    print("One condition is true here")

print('----------------')

print ("Nested if:\n")

a = 40
if a>10:
    print("40 is always > 10")
    if a>20:
        print("40 is always > 20")
else:
     print("Don't get the chance to display this ever.")