# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

# greetings to the user
print ("\n\033[1m| GUESS THE NUMBER GAME |\033[0m \n\n\033[1m\033[95mDirection:\033[0m This program will generate a \033[4mrandom number from 0 to 100.\033[0m You are to guess it correctly. If you don't, you'll be asked repeatedly. Don't worry, we'll provide some hints.")

# code for generating random number from 0-100
from random import randrange
randomNum = randrange(0, 100)

userGuess = int(input("\n\033[1m\033[96mEnter your guess here: \033[0m"))

# a code block that will ask the user repeatedly until the random number has been guessed correctly
while randomNum != userGuess:
    if userGuess > randomNum:
        userGuess = int(input("Your guess is \033[93mgreater than\033[0m the number. Try \033[93mdecreasing\033[0m your numerical input. \n\n\033[1m\033[96mEnter your guess here: \033[0m"))
        if userGuess == randomNum:
            break
    elif userGuess < randomNum:
        userGuess = int(input("Your guess is \033[93mless than\033[0m the number. Try \033[93mincreasing\033[0m your numerical input. \n\n\033[1m\033[96mEnter your guess here: \033[0m"))
        if userGuess == randomNum:
            break

# if the user guessed the number correctly
if userGuess == randomNum:
    print (f"\n\033[1m\033[92mYou're correct!\033[0m \nThe answer is \033[1m{randomNum}\033[0m.\n")