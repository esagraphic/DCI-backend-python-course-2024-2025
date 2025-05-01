import random

def get_guess():
    guess = ""
    while guess not in ("heads", "tails"):
        print("Guess the coin toss! Enter heads or tails:")
        guess = input().lower()
    return guess


def map_guess_to_number(guess):
    return 1 if guess == "heads" else 0


guess = get_guess()
toss = random.randint(0, 1) 


if toss == map_guess_to_number(guess):
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = get_guess()  # Ask for the second guess
    if toss == map_guess_to_number(guess):
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
