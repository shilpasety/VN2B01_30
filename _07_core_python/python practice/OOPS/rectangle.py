'''Write a Python class named Rectangle constructed by a length and width and a
method which will compute the area of a rectangle.'''

class Rectangle:
    def __init__(self, l, w):
        l=int(input("Enter length:"))
        w=int(input("Enter width:"))
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

obj = Rectangle(1,1)
print("The area of the rectangle is:",obj.area())