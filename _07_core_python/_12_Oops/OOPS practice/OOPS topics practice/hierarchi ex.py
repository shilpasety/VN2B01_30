class Father:

    def __init__(self,fname,sname):
        self.fname = fname
        self.sname = sname

    def get_fname(self):
        print("The father's name:",self.fname,self.sname)

class child1(Father):

    def __init__(self,c1name):
        super().__init__('Kishor', 'Devi')
        self.c1name = c1name

    def get_c1name(self):
        print("Child1 name:",self.c1name,self.sname)
        super().get_fname()


class child2(Father):

    def __init__(self, c2name):
        super().__init__('Kishor','Devi')
        self.c2name = c2name

    def get_c2name(self):
        print("Child2 name:",self.c2name, self.sname)
        super().get_fname()

ob = child2('Pranaya')
ob.get_c2name()


ob1 = child1('Advaitha')
ob1.get_c1name()




