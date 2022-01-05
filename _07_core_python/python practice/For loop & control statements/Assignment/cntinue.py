a = int(input("Enter 'a' value:"))
r= int(input("Enter 'r' value:"))
n= int(input("Enter 'n' value:"))
pro=0
for i in range(n+1):
    pro =pro+ a*(r**i)
print("Total is:",pro)

