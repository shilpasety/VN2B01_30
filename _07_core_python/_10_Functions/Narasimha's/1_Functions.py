# What is Function

# Function is block of code which executed when it is called.

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))


def tot(c, d):

    e = c + d
    print("Sum of two numbers :--", e)


tot(5, 6)
tot(a, b)

print("------Without Return Type------")


def ttl(m, n):
    p = m + n
    print("Sum is :--", p)


ttl(7, 1)
ttl(9, 5)
print("Sum is :--", ttl(19, 45))


print("------With Return Type------")


def tol(j, k):
    m = j + k
    return m


print("Total is :--", tol(34, 89))
print(tol(45, 27))
tol(345, 19)

print("---------Examples for Without Return Type----------")

o = [12, 34, 546, 243, 657]
print("List is :--", o)
print(o.append(56))
print("List After adding :--", o)
print(o.remove(34))
print("List After Removing :--", o)

print("-------Examples for With Return Type--------")
print("Index Value of '546' is :--", o.index(546))
print("Deleted Value is :--", o.pop())
print("Deleted Value at '2' Index is :--", o.pop(2))
print(o)
