class A:

    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print("Feature 2 is working")

class B:

    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):  #It access all the properties of A & B as B

    @staticmethod
    def feature5():
        print("Feature 5 is working")

p3 = C()
p3.feature5()
p3.feature1()
p3.feature4()