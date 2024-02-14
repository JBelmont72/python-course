'''RPS_2 will add a While loop so that the game keeps playing

at 2:58 on tape
command control spacebar for emojis!

Can highlight a command or word  then press command +F and it will show how many times that occurs and where
\n to replace print(' ') if just want an empty line

this might be a good follow on course after dave gray
https://www.youtube.com/@LearningOrbis

'''
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
playagain = True
while True:
    
    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\nf")
    

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")
    playagain = input('\nPlayagain?\n\t Y for yes\n\t Q for Quit\n\n')
                                
    if playagain.lower() =='y':
        continue
    else:
        print("\n 😇🥰😱")
    break
    # playagain = False ## also works instead of break  same effect
sys.exit('😅')
# print("")
# playerchoice = input(
#     "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

# player = int(playerchoice)

# if player < 1 or player > 3:
#     sys.exit("You must enter 1, 2, or 3.")

# computerchoice = random.choice("123")

# computer = int(computerchoice)

# print("")
# print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
# print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
# print("")

# if player == 1 and computer == 3:
#     print("🎉 You win!")
# elif player == 2 and computer == 1:
#     print("🎉 You win!")
# elif player == 3 and computer == 2:
#     print("🎉 You win!")
# elif player == computer:
#     print("😲 Tie game!")
# else:
#     print("🐍 Python wins!")
