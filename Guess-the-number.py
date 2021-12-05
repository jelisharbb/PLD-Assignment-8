# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

# greetings to the user
print ("\nGUESS THE NUMBER GAME \n\nDirection: This program will generate one random number from 0 to 100. You should guess it correctly. Otherwise, you would be asked repeatedly. Don't worry, we will give you some hints.")

# code for generating random number from 0-100
from random import randrange
randomNum = randrange(0, 100)

userGuess = int(input("\nEnter your guess here: "))

# a code block that will ask the user repeatedly until the random number has been guessed correctly
while randomNum != userGuess:
    if userGuess > randomNum:
        userGuess = int(input("Your input number is greater than the number. Try decreasing your numerical input. \n\nEnter your guess here: "))
        if userGuess == randomNum:
            break
    elif userGuess < randomNum:
        userGuess = int(input("Your input number is less than the number. Try increasing your numerical input. \n\nEnter your guess here: "))
        if userGuess == randomNum:
            break

# if the user guessed the number correctly
if userGuess == randomNum:
    print (f"\nYou're correct! \nCorrect answer: {randomNum}\n")