class Parent:
    parentAttr = 100

    def __int__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAtter(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print(Parent.parentAttr)


class Child(Parent):
    def __int__(self):
        print("calling child constructor")


child = Child()
child.parentMethod()
child.setAtter(200)
child.getAttr()
