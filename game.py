"""A number-guessing game."""

# Put your code here
# print("hello!")

# psuedocode:
# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player

from random import randint


tries = 0
number = randint(1, 100)

print("Hello! What's your name?")

name = input("Type your name here: ")

print(f"{name}, I'm thinking of a number between 1 and 100. \nCan you guess what the number is?")

while True:
    guess = input("Enter your number guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print(f"{guess} is not a valid number, try again.")
        continue

    if guess < 1 and guess > 100:
        print("Please guess a number between 1 and 100. Try again.")
        continue
    
    tries += 1

    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again")
    else:
        print(f"Congrats {name}! \nYou guessed my number in {tries} attempts!")
        break

