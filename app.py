def magic_string(_count=[0]):
    _count[0] += 1
    return ", ".join(["Best School"] * _count[0])

print(magic_string())