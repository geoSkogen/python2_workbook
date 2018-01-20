class Parent(object):
    parentAttr = 100
    def __init__(self):
        print("initializing parent constructor")

    def parentMeth(self):
        print("parent method call recieved")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print(Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("initializing child constructor")
    def childMeth(self):
        print("child method call recieved")

c = Child()
c.childMeth()
 #object c has access to vars & meths in Parent
c.parentMeth()
c.setAttr(237)
c.getAttr()
