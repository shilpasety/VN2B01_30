print("Using continue statement to skip")
y= int(input("Enter a number:"))
for i in range(1,11):
    x=y*i
    if(i==5 or i==10):
        continue
    print(y,"X",i,"=",x)
print('----------------------------------')
print("Using break statement to come out of loop")
z= int(input("Enter a number:"))
for i in range(1,10):
    x=z*i
    if(i==6):
        break
    print(z,"X",i,"=",x)
print("Came out of the loop")
