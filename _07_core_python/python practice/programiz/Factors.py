f = int(input("Enter a number:"))
print("The factors of",f,"are::")
for i in range(1,f+1):
    if f%i==0:
        print(i,end=' ')