number = int(input("Number: "))
for i in number:
    if number % 1 == 0 or number % number == 0:
        print("Prime number")
    else:
        print("Not prime number")
