#What is Inheritance:
#       It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods
#       by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the
#       properties from another class. 

#create a Inheritance Syntix:
class BaseClass:
    pass
class Derivedclass(BaseClass):
    pass


#create a Inheritance program:

class A:
    def __init__(self,name,age,company) -> None:
        self.name=name
        self.age=age
        self.company=company
    def m(self):
        print(f"Hi i am {self.name}")
        print(f"I am {self.age} Years old")
        print(f"I am working {self.company} company")
class B(A):
    def __init__(self, name, age, company,loaction) -> None:
        super().__init__(name, age, company)
        self.location=loaction

    def k(self):
        print(f"Hi i am {self.name}")
        print(f"I am {self.age} Years old")
        print(f"I am working {self.company} company")
        print(f"Location is {self.location}")



obj=A("Milan Panja",23,"TATA")
obj1=B("Milan Panja",23,"TATA","KOlkata")
obj.m()
obj1.k()

#--------------------There are 5 different types of inheritance in Python:---------------------------

#1.Single inheritance: 
# When a child class inherits from only one parent class, it is called single inheritance.
#  We saw an example above.

#Single Inheritance Syntix:
class BaseClass:
    pass
class Derivedclass(BaseClass):
    pass

#2 Multiple inheritances: 
#   When a child class inherits from multiple parent classes, it is called multiple inheritances. 
#Multiple Inheritance Syntix:

class A:
    def __init__(self,name) -> None:
        self.name=name
    def print(self):
        print(self.name)
class B(A):
    def __init__(self, name,age) -> None:
        super().__init__(name)
        self.age=age
    def print1(self):
        print(self.name)
        print(self.age)
class D(B,A):
    def __init__(self, name, age,company) -> None:
        super().__init__(name, age)
        self.company=company
    def print3(self):
        print(self.name,self.age,self.company)
   
obj=A("Milan Panja")
obj1=B("Arindam Panja",23)
obj2=D("Arindam Panja",23,"TATA")
obj.print()
obj1.print1()
obj2.print3()
        
#3.Multilevel inheritance:
#When we have a child and grandchild relationship. This means that a child class will inherit from
#its parent class, which in turn is inheriting from its parent class.

#Multilevel Inheritance Syntix:

class A:
    def __init__(self,name) -> None:
        self.name=name
    def getname(self):
        return self.name
class B(A):
    def __init__(self, name,age) -> None:
        super().__init__(name)
        self.age=age
    def getage(self):
        return self.age
class D(B):
    def __init__(self, name, age,address) -> None:
        super().__init__(name, age)
        self.address=address
    
    def getaddress(self):
        return self.address
obj=D("Milan Panja",23,"Paschim Medinipur")
print(obj.getname(),obj.getage(),obj.getaddress())

#4.Hierarchical inheritance:
#More than one derived class can be created from a single base.

#Hierarchical Inheritance Syntix:
 
class C(object):
    def __init__(self):
        self.c = 21
        self.__d = 42 #private
class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)
 
object1 = D()

print(object1.c)
print(object1.__d)

#5.Hybrid inheritance:
#This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.

#Hierarchical Inheritance Syntix:

class A:
    def k(self):
        print("Hi I am Milan Panja")
class B(A):
    def k1(self):
        print("Hi i am Ankit")
class D(A):
    def k2(self):
        print("Hi i am Animas")
class F(B,D):
    pass

obj=F()
obj.k()
obj.k1()
obj.k2()