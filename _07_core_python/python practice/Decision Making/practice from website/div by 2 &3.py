'''Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.'''
d = int(input("Enter a number:"))
if d%2==0 and d%3==0:
    print(d,"is divisible by both 2 & 3")
else:
    print("Not")