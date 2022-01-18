'''Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other
 than 1 and itself.'''
n=int(input("Enter a number:"))
def prime(n):
    c=0
    if n==1:
        print("1 is not a prime number")
    else:
        for i in range(1,n):
            if n%i==0:
                c+=1
        if c>=3:
            print(n,"is not prime number")
        else:
            print(n,"is prime number")
prime(n)
