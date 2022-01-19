print("---------Function Categories---------")
print("1) Function with parameters, with return type")


def tol(a, b):
    c = a + b
    return c


print(tol(12, 45))
print("Total is :--", tol(23, 56))

print("2) Function with parameters, without return type")


def tot(d, e):
    f = d + e
    print("Sum is :--", f)


tot(45, 23)
tot(234, 356)
print("Sum is :--", tot(234, 345))

print("3) Function without parameters, with return type")


def add():
    j = 30
    k = 40
    m = j + k
    return m


s = add()
print("Addition is :--", s)

print("4) Function without parameters, without return type")


def ttl():
    t = 50
    u = 60
    v = t + u
    print("Result is :--", v)


ttl()