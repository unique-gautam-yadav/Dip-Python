
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printVal(self):
        print(self.name, self.age)

    def isEmp(self):
        print(True)


class Student(Person):
    def isEmp(self):
        print(False)
    pass


obj1 = Person("Gautam", 17)
obj1.isEmp()
obj = Student("Gautam", 17)



obj.printVal()
obj.isEmp()
