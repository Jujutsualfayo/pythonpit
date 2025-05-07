a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))  # Memory address of object 'a'
print(id(b))  # Different object, same content, so different id
print(id(c))  # Same object as 'a', so same id
