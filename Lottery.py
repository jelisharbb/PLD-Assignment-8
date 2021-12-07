# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

from random import randrange

# looping (if the user wants to play again)
restart = True
while restart:

    # generating three lucky numbers
    luckyNum1 = randrange (0, 9)
    luckyNum2 = randrange (0, 9)
    luckyNum3 = randrange (0, 9)

    # looping (if the generated lucky numbers have duplication)
    luckyNumDup = False
    while not(luckyNumDup):
        if luckyNum1 == luckyNum2:
            luckyNum2 = randrange (0, 9)
        elif luckyNum1 == luckyNum3 or luckyNum2 == luckyNum3:
            luckyNum3 = randrange (0, 9)
        else:
            luckyNumDup = True
            break
    luckyNum123 = luckyNum1, luckyNum2, luckyNum3

    # greeting to the user
    print ("\nWELCOME TO PEPITO MANA-LOTTERY \n")

    # looping (if the user input is either an alphabet or a number beyond the scope)
    userNum1Loop = False
    while not(userNum1Loop):
        userNum1 = input("(1) Pick a number from 0 to 9  : ")
        if userNum1.isdigit():
            userNum1Fnl = int(userNum1)
            if userNum1Fnl <= 9 and userNum1Fnl >= 0:
                userNum1Loop = True
            else:
                print ("Your input is beyond the scope of the lottery. Please choose a number from 0 to 9 only.")
                userNum1Loop = False
        else:
            print ("Please input numerical value only.")
            userNum1Loop = False

    # looping (if the user input is either an alphabet, a number beyond the scope, or a duplicate number)
    userNum2Loop = False
    while not(userNum2Loop):
        userNum2 = input("(2) Pick a number from 0 to 9  : ")
        if userNum2.isdigit():
            userNum2Fnl = int(userNum2)
            if userNum2Fnl == userNum1Fnl:
                print ("You cannot enter same numbers. Please choose another number.")
                userNum2Loop = False
            elif userNum2Fnl <= 9 and userNum2Fnl >= 0:
                userNum2Loop = True
            else:
                print ("Your input is beyond the scope of the lottery. Please choose a number from 0 to 9 only.")
                userNum2Loop = False
        else:
            print ("Please input numerical value only.")
            userNum2Loop = False

    userNum3 = input("(3) Pick a number from 0 to 9  : ")
    userNum123 = userNum1, userNum2, userNum3
    print (f"Your numbers: {userNum1}, {userNum2}, {userNum3}")

    if sorted(luckyNum123) == sorted(userNum123):
        playAgain = input(f"You won! \nThe winning numbers are [{luckyNum1}, {luckyNum2}, {luckyNum3}] \nDo you want to play again? (Type Y if Yes and N if No) ")
    else:
        playAgain = input(f"You lose. \nThe winning numbers are [{luckyNum1}, {luckyNum2}, {luckyNum3}] \nDo you want to play again? (Type Y if Yes and N if No) ")