secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    if guess == secret_number:
        guess += 1
        print("You won")
