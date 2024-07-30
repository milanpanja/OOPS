#The word polymorphism means having many forms. In programming, polymorphism means the same function
#  name (but different signatures) being used for different types.
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")
ob_in=India()
ob_us=USA()
for i in (ob_in,ob_us):
    i.capital()
    i.language()
    i.type()

#--------------------

class A:
    def name(self):
        print("Hi I am Milan Panja")
    def age(self):
        print("My age 23")
class B(A):
    def age(self):
        print("My age 24")
class N(A):
    def name(self):
        print("My name is jjj")
ob=A()
ob1=B()
ob2=N()

ob.name()
ob.age()

ob1.name()
ob1.age()

ob2.name()
ob2.age()
        