# Class : Group of objects
# Object : Copy of a class, Who is able to access class variables and functions
# Inheritance
# Abstraction
# Polymorphism
# Constructor

class Student:
    # self refer to current instance/object
    # Below is method or function
    def getDetails(self):
        print(self.name)
        print(self.rollNo)

obj1 = Student()
obj2 = Student()
obj3 = Student()

obj1.name = 'Elia'
obj1.rollNo=1

obj2.name = 'Niki'
obj2.rollNo=2

obj3.name = 'Rahi'
obj3.rollNo=3

# obj1.getDetails()
# obj2.getDetails()
# obj3.getDetails()

# print(f"Variable outside class: {obj1.name}")
# print(getattr(obj1, 'names', 'No Name'))

# setattr(obj1, 'city', 'London')

# print(getattr(obj1, 'city', 'NO CITY'))

print(hasattr(obj1, 'name'))

delattr(obj1, 'name')

print(hasattr(obj1, 'name'))
















