weight = int(input("Input weight: "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "L":
    converted = weight * 0.455
    print(f"(Your weight is {converted} kilos)")
else:
    if unit.upper() == "K":
        converted = weight / 0.455
        print(f"(Your weight is {converted} pounds)")
        

