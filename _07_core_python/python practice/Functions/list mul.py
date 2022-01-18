'''Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336'''
print('-----------------My own trail---------------------')
print()
lst = [8,2,3,-1,7]
print(lst)
def lst_mul(lst1):
    mul = 1
    for m in lst1:
        mul = mul*m
    return mul
m = lst_mul(lst)
print("Multiplication of all the elements in list is:",m)
print()

print('----------------Efficient method-------------------------')
print()
def lmul(items):
    print(type(items))
    m=1
    for k in items:
        m*=k
    return m
print(lmul([8,2,3,-1,7]))



