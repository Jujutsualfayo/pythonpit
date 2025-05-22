class Student:
    def __init__(self, name, age, cohort, grade):
        self.name = name
        self.age = age
        self.cohort = cohort
        self.grade = grade

    def __str__(self):
        return(
            f"Name: {self.name}\nAge: {self.age}"
            f"Cohort: {self.cohort}\nGrade: {self.grade}"
        )
    def grading_hist(self, your_grad, option="Next class"):
        if self.grade == grading_hist:
        return(
           print(f"Hello {self.name}\nYour score is {your_grad}\n"), 
           print(f"You pass to the {option}")
        )
student_1 = Student("Francis Nyatundo", 24, 22, "Aggrey house")
student_1.grading_hist(90)
print(student_1.grading_hist)
