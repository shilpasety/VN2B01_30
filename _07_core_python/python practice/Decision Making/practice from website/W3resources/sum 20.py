'''Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20'''

a= int(input("Number1:"))
b= int(input("Number2:"))

sum = a+b
l = [15,16,17,18,19,20]
if sum in l:
    print(20)
else:
    print(sum)
