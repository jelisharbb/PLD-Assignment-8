# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

# greetings to the user
print ("\nGUESS THE NUMBER GAME")

# code for generating random number from 0-100
from random import randrange
randomNum = randrange(0, 100)

userGuess = int(input("\nEnter your guess here: "))