# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

from random import randrange

luckyNum1 = randrange (0, 9)
luckyNum2 = randrange (0, 9)
luckyNum3 = randrange (0, 9)

print ("\nWELCOME TO PEPITO MANA-LOTTERY \n")

userNum1 = input("(1) Pick a number from 0 to 9  : ")
userNum2 = input("(2) Pick a number from 0 to 9  : ")
userNum3 = input("(3) Pick a number from 0 to 9  : ")