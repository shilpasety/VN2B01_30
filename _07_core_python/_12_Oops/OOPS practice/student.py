class Student:
    def __init__(self, student_id, student_name,class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name
    def meth(self,a):
        print("It is a function only "+a)

stu  = Student(102,'Advaitha',2)
print(stu.student_id)
print(stu.student_name)
print(stu.class_name)

stu.meth("Hurray")