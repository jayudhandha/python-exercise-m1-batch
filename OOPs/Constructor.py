class Student:
    name=""
    rollNo=0
    city=""

    # It's a special method to initialize the class variables
    # Constructor will be called automatically when we create object of class
    # def __init__(self):
    #     print("Construcotr called")

    def __init__(self, name, rollNo):
        print("Construcotr called")
        self.name = name
        self.rollNo = rollNo

    # self refer to current instance/object
    # Below is method or function
    def getDetails(self):
        print(self.name)
        print(self.rollNo)
        print(self.city)

obj1 = Student("Elia", 1)
obj2 = Student("Jayesh", 2)

obj1.city = 'Vadodara'

obj1.getDetails()
obj2.getDetails()