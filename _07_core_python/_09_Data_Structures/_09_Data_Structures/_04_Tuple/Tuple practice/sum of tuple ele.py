s=int(input("Enter the size::"))
l=[]
print("Enter the values into tuple:")
for q in range(s):
    v = int(input())
    l.append(v)
t = tuple(l)
print(t)
sum=0
for j in range(s):
    sum = sum+t[j]
print("The sum of tuple values::",sum)