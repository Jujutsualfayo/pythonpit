class Student:
    def __init__(self, name, age, cohort, dorm):
        self.name = name
        self.age = age
        self.cohort = cohort
        self.dorm = dorm

    def __str__(self):
        return
    f"Name: {self.name}\nAge: {self.age}"
    f"Cohort: {self.cohort}\nDorm: {self.cohort}"
student_1 = Student("Francis Nyatundo", 24, 22, "Aggrey house")
print(student_1.name)
