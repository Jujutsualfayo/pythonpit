# test_base_model.py

from models.base_model import BaseModel

# Create an instance
b = BaseModel()

# Print the object
print(b)

# Call save() and print again to see updated time
b.save()
print(b)

# Convert to dictionary and print
print(b.to_dict())
