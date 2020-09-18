class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.age = 0
        self.marks = 0

    def display(self):
        print("Name", self.name)
        print("Roll No", self.roll_no)
        print("Age", self.age)
        print("Marks", self.marks)

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

s1 = Student("Sahil", 12)
s1.setAge(20)
s1.setMarks(90)
s1.display()

s2 = Student("Rohit", 20)
s2.display()