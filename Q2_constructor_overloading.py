
class Student:
    def __init__(self, roll, name=None, percent=None):
        self.roll = roll
        self.name = name
        self.percent = percent

    def display(self):
        print("Roll:", self.roll)
        if self.name:
            print("Name:", self.name)
        if self.percent:
            print("Percentage:", self.percent)
        print()

s1 = Student(1)
s2 = Student(2, "Amit")
s3 = Student(3, "Riya", 82.5)

s1.display()
s2.display()
s3.display()
