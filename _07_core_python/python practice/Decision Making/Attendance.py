wd =261
name = input("Enter the student name: ")
ab = int(input("Enter the absent days:"))
pre = int(((wd-ab)/wd)*100)
if(pre>75):
    print(name,"can attend the interview with",pre,"%")
else:
    print(name,"can't attend the interview with",pre,"%")