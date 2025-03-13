student = {"age":"25", "weight":"50kg", "school":"Alliance school"}
print(student.get("age"))
student["age"] = 26
print(student.get("age"))
if "age" in student:
    print("Exists")