#Encapsulation:
#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
#It describes the idea of wrapping data and the methods and variable that work on data within one unit.

#
class Base:
    def __init__(self):

        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ",self._a)
        self._a = 3
        print("Calling modified protected member outside class: ",self._a)


obj1 = Derived()

obj2 = Base()

print("Accessing protected member of obj1: ", obj1._a)

print("Accessing protected member of obj2: ", obj2._a)