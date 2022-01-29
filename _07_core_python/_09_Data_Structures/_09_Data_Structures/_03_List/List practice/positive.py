# Print positive numbers in list

po = [1,2,-3,-4,5,6]
po1=[]
for i in po:
 if i>0:
  po1.append(i)
print(po1)

#print after removing the duplicates

du = [10,10,20,30,20,40,30,50,60]
new = []
for k in range(len(du)):
 j=k+1
 for j in range(1,len(du)):
  if du[k]==du[j] not in new:
   new.append(du[k])
print(new)

