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


print('Child class features\n')

p2 = B()
p2.feature1()
p2.feature2()
p2.feature3()
p2.feature4()
