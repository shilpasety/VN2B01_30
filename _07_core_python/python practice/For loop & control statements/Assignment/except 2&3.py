print("The numbers between 1 and 20 that are not multiples of 2 &3:")
for m in range(1,20):
    if(m%2==0 or m%3==0):
        continue
    print(m)
