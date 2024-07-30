#What is class:
# A class is a user-defined blueprint or prototype from which objects are created.
#create a class:

class Dog:
    sound="Bark"

#What is Object:
# Objects are variables that contain data and functions that can be used to manipulate the data..
#create a Object:

obj=Dog()
print(obj.sound)

#================

class Dog:
    att="kk"
    att1="kk2"
    def m(self):
        print(f"I am {self.att}")
        print(f"I am {self.att1}")
obj=Dog()
print(obj.att)
obj.m()


