i=10
if i<15 :
    print("10 is < 15")
    print("As I'm following the indentation am still in  if")
print("I am not in if")

print ('--------------------------')

i=10
if i>15 :
    print("10 is < 15")
    print("As I'm following the indentation am still in  if")
    if i<15:
        print("Doesn't get the chance to execute as still in false if stmnt")
print("I am not in if")

print ('--------------------------')

i=10
if i<15 :
    print("10 is < 15")
    print("As I'm following the indentation am still in  if")
    if 'True':
        print("Got the chance bcz the above if is true")
print("I am not in if")


print ('--------------------------')

i=10
if i>15 :
    print("10 is < 15")
    print("As I'm following the indentation am still in  if")
if 'True':
        print("Not related to the above if at all bcz not in indentation")
print("I am not in if")