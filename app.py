person = {"name": "Alice", "age": 25, "city": "New York"}
person ["age"] = 30
person ["job"] = "engineer"
print(person.get("job"))
if "salary" in person:
    print("Exists")
else:
    print("Does not exists")