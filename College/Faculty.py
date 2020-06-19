class Student:
    def __init__(self, branch, subject):
        print("Construcotr called")
        self.branch = branch
        self.subject = subject

    def getDetails(self):
        print(self.branch)
        print(self.subject)

