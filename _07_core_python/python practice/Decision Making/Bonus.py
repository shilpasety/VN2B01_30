sal = int(input("Enter the salary:"))
ser = int(input("Enter the years of service:"))
if(ser>10):
    bonus = int(0.1*sal)
    print("As the service is more than 10 years you get",bonus,"/-","as bonus")
elif(ser>=6 and ser<=10):
    bonus = int(0.08*sal)
    print("As per your service you get",bonus,"/-","as bonus")
elif(ser<6 and ser>0):
    bonus = int(0.05*sal)
    print("As per your service you get",bonus,"/-","as bonus")
else:
    print("No Bonus")
