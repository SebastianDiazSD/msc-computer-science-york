"""
Write a program that asks the user to guess a number between 1 and 10. The program should keep asking until the user
guesses the correct number. After each attempt, the program should display a message indicating if the guess is too low
or too high.

"""

# Generate a random number between 1 and 10

import random

number_to_guess = random.randint(1, 10)
print(number_to_guess)
# Get inputs from user

number_guessed = int(input("Guess a number between 1 and 10: "))

# Determine if the guess is correct

user_guessed = False

while user_guessed is False:
    if number_guessed < number_to_guess:
        print("The number you guessed is too low")
        number_guessed = int(input("Guess again number between 1 and 10: "))
    elif number_guessed > number_to_guess:
        print("The number you guessed is too high")
        number_guessed = int(input("Guess again number between 1 and 10: "))
    else:
        print("You guessed the number")
        user_guessed = True
