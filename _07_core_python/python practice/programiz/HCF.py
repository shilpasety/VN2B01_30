x= int(input("Enter First number:"))
u= int(input("Enter Second number:"))
if x>u:
    smaller = u
else:
    smaller = x
for i in range(1,smaller+1):
    if(x%i==0 and u%i==0):
        hcf = i
print("The HCF of",x,"and",u,"is:",hcf)
