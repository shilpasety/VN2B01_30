class parent:

    @staticmethod
    def feature1():
        print('Parent class is working')



class child1(parent):

    @staticmethod
    def feature3():
        print('In child class1')



class child2(parent):

    @staticmethod
    def feature5():
        print("In child class2")

p1 = child1()
p1.feature1()
p1.feature3()

p2 = child2()
p2.feature1()
p2.feature5()