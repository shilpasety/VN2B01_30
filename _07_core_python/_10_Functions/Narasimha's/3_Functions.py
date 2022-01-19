print("----------Passing Arguments----------")

print("-------1) Positional Arguments-------")


def add(n1, n2, n3):
    a = n1 + n2 + n3
    print("Sum is :--", a)


add(14, 43, 67)
add(56, 34, 23)

print("-------2) Default Arguments-------")


def tot(n1, n2=50, n3=4):
    b = n1 + n2 + n3
    print("Total is :--", b)


tot(34, 67, 19)
tot(67, 23)

print("------3) Keyword Arguments-------")


def tol(n1, n2, n3):
    c = n1 + n2 + n3
    print("Total :--", c)


tol(n2=40, n1=15, n3=25)
tol(n3=5, n1=15, n2=20)


