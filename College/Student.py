class Student:
    # Abstraction is data hiding
    __college = "SVIT"

    def __init__(self, name, rollNo):
        print("Construcotr called")
        self.name = name
        self.rollNo = rollNo

    def getDetails(self):
        print(self.name)
        print(self.rollNo)
        print(Student.__college)

    def getHisMarks(self):
        print(f"Studenf from {self.college} college got good marks")

obj1 = Student("Elia", 1)
obj2 = Student("Rahi", 2)
obj3 = Student("Niki", 3)

obj1.getDetails()
obj2.getDetails()
obj3.getDetails()