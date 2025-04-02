def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
number = int(input("Insert number: "))
print_last_digit(number)
print()




