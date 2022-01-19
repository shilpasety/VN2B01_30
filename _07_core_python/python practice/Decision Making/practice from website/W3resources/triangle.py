'''Write a Python program to check a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:
x: 6
y: 8
z: 12
Scalene triangle '''

print('Input lengths of the triangle sides:')
x  = int(input('x:'))
y  = int(input('y:'))
z  = int(input('z:'))

if x==y==z:
    print('Equilateral Triangle')
elif x==y or y==z or x==z:
    print('isosceles Triangle')
else:
    print('Scalene Triangle')