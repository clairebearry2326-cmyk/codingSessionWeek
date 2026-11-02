import random

# Pick a secret number from 1 to 100.
secret_number = random.randint(1, 100)
guess_count = 0

# Keep asking until the guess is correct.
while True:
    guess = int(input("Guess a number from 1 to 100: "))
    guess_count = guess_count + 1

    if guess < secret_number:
        print("HIGHER")
    elif guess > secret_number:
        print("LOWER")
    else:
        print("Correct! You guessed it in", guess_count, "guesses.")
        break
