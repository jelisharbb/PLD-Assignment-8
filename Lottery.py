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
    # list of lucky numbers    
    luckyNumList = luckyNum1, luckyNum2, luckyNum3

    # greeting to the user
    print ("\n\033[1m| WELCOME TO PEPITO MANA-LOTTERY |\033[0m\n")

    # looping for 1st number (if the user input is either an alphabet or a number beyond the scope)
    userNum1Loop = False
    while not(userNum1Loop):
        userNum1 = input("\033[1m\033[96m(1) Pick a number from 0 to 9  :\033[0m ")
        if userNum1.isdigit():
            userNum1Fnl = int(userNum1)
            if userNum1Fnl <= 9 and userNum1Fnl >= 0:
                userNum1Loop = True
            else:
                print ("Your input is \033[4mbeyond the scope\033[0m of the lottery. Please choose a number from \033[4m0 to 9\033[0m only.")
                userNum1Loop = False
        else:
            print ("Please input \033[4mnumerical value\033[0m only.")
            userNum1Loop = False

    # looping for 2nd number (if the user input is either an alphabet, a number beyond the scope, or a duplicate number)
    userNum2Loop = False
    while not(userNum2Loop):
        userNum2 = input("\033[1m\033[96m(2) Pick a number from 0 to 9  :\033[0m ")
        if userNum2.isdigit():
            userNum2Fnl = int(userNum2)
            if userNum2Fnl == userNum1Fnl:
                print ("You \033[4mcannot\033[0m enter \033[4msame\033[0m numbers. Please choose another number.")
                userNum2Loop = False
            elif userNum2Fnl <= 9 and userNum2Fnl >= 0:
                userNum2Loop = True
            else:
                print ("Your input is \033[4mbeyond the scope\033[0m of the lottery. Please choose a number from \033[4m0 to 9\033[0m only.")
                userNum2Loop = False
        else:
            print ("Please input \033[4mnumerical value\033[0m only.")
            userNum2Loop = False

    # looping for 3rd number (if the user input is either an alphabet, a number beyond the scope, or a duplicate number)
    userNum3Loop = False
    while not(userNum3Loop):
        userNum3 = input("\033[1m\033[96m(3) Pick a number from 0 to 9  :\033[0m ")
        if userNum3.isdigit():
            userNum3Fnl = int(userNum3)
            if userNum3Fnl == userNum1Fnl or userNum3Fnl == userNum2Fnl:
                print ("You \033[4mcannot\033[0m enter \033[4msame\033[0m numbers. Please choose another number.")
                userNum3Loop = False
            elif userNum3Fnl <= 9 and userNum3Fnl >= 0:
                userNum3Loop = True
            else:
                print ("Your input is \033[4mbeyond the scope\033[0m of the lottery. Please choose a number from \033[4m0 to 9\033[0m only.")
                userNum3Loop = False
        else:
            print ("Please input \033[4mnumerical value\033[0m only.")
            userNum3Loop = False

    # list of user inputed numbers
    userNumList = int(userNum1), int(userNum2), int(userNum3)
    print (f"\nYour numbers: {int(userNum1)}, {int(userNum2)}, {int(userNum3)}")

    # if the user won
    if sorted(luckyNumList) == sorted(userNumList):
        playAgain = input(f"\n\033[92m\033[1mY O U  W O N !\033[21m\033[0m \nThe winning numbers: {luckyNum1}, {luckyNum2}, {luckyNum3} \n\nDo you want to play again? (Type Y if Yes and N if No)\n")
        # if the user wants to play again
        if playAgain.upper() == 'Y':
            restart = True
        elif playAgain.upper() == 'N':
            restart = False
            break

    # if the user lose
    else:
        playAgain = input(f"\n\033[1m\033[91mY O U  L O S E .\033[0m \nThe winning numbers: {luckyNum1}, {luckyNum2}, {luckyNum3} \n\nDo you want to play again? (Type Y if Yes and N if No)\n")
        if playAgain.upper() == 'Y':
            restart = True
        elif playAgain.upper() == 'N':
            restart = False
            break

print ("\n\033[1m\033[95mTHANK YOU FOR PLAYING! COME AGAIN. (•ᴗ•)\033[0m\n")