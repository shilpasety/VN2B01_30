num=int(input("Enter the percentage:"))
if(num>=80 and num<=100):
    print("A+ Grade")
elif(num>=60 and num<80):
    print("A Grade")
elif(num>=50 and num<60):
    print("B+ Grade")
elif(num>=45 and num<50):
    print("B Grade")
elif(num>=25 and num<45):
    print("C Grade")
elif(num<25):
    print("D Grade")
else:
    print("Percentage should be <100%")