class A:

    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print("Feature 2 is working")

class B(A):  # Child class inheriting parent class A, It acquires all the properties of A
            # By creating on object for child class we can access parent class properties

    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print("Feature 4 is working")

class C(B):  # class C is an grand child of A, It access all the properties of A & B as B is inheriting the
            # properties of A

    def feature5(self):
        print("Feature 5 is working")


p3 = C()
p3.feature5()
p3.feature1()
p3.feature4()