#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# How to Use Self parameter
class A:
    def __init__(self,name,company):
        self.name=name
        self.company=company
    def M(self):
        print(f"Hi i am {self.name}")
        print(f"And i am Working for {self.company} company")
obj=A("Milan Panja","TATA")
obj.M()

#__inti__ methord(initializing)
# __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s state
class B:
    def __init__(self,name):
        self.name=name
    def j(self):
        print(f"Hi My name is {self.name}")
obj=B("Milan Panja")
obj.j()

#__str__ methord
# __str__()that is used to define how a class object should be represented as a string.

class B:
    def __init__(self,name) -> None:
        self.name=name
    def __str__(self):
        return f"Hi My name is {self.name}"
obj=B("Milan Panja")
print(obj)

#===============


class Dog:

    # Class Variable
    animal = 'dog'
    # The init method or constructor
    def __init__(self, breed):

        # Instance Variable
        self.breed = breed

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color
# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())

