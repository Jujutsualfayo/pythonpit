class Student:
    def __init__(self, name, age, cohort, dorm):
        self.name = name
        self.age = age
        self.cohort = cohort
        self.dorm = dorm
student_1 = Student("Francis Nyatundo", 24, 22, "Aggrey house")
print(student_1.name)
