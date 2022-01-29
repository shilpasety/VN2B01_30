'''Example for Multiple Inheritance'''
class Mother:

    sirname = 'Muddam'

    def __init__(self):
        self.mname = 'Shilpa'

    def show(self):
        print("Mother's name:",self.mname,Mother.sirname)

class Father:

    sname = 'Devi'

    def __init__(self):
        self.fname = 'Kishor'

    def show(self):
        print("Father's name:", self.fname, Father.sname)

class child(Father,Mother):

    def __init__(self):
        super().__init__()
        self.bname = 'Advaitha'

    def baby(self):
        print("The baby's name is:",self.bname,self.fname)

c = child()
c.show()
c.baby()

m= Mother()
m.show()

