'''Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the
 guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.'''

n=int(input("Enter a number:"))
while(True):
    if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
        print("Well guessed!")
        break
    else:
        n = int(input("Enter a number:"))