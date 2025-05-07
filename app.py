items = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
for item in items:
    try:
        print(len(item))
    except TypeError:
        print("Item has no length:", item)