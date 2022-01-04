print("The numbers divisible by 11 but not by 2 are:")
for k in range(100,500):
    if (k%11==0 and k%2!=0):
        print(k,end=' ')