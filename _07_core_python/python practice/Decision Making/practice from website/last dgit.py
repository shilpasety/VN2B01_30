''' Write a program to display the last digit of a number.
 Write a program to check whether the last digit of a number( entered by user ) is
divisible by 3 or not.
'''

l = int(input("Enter a number:"))
d = l%10
if d%3==0:
    print("Last digit is divisible by 3")
else:
    print("Not divisible by 3")

