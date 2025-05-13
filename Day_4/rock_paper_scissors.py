# Randomisation and Python Lists
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)  
'''

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))
picker = [rock, paper, scissors]

if 0 <= player < 3:
    print("You Chose:")
    print(picker[player])
else:
    print("Invalid Number")
    exit()

bot = random.randint(0, 2)
print("Computer Chose:")

print(picker[bot])

if player == bot:
    print("You Draw")
elif (player == 2 and bot == 1) or (player == 1 and bot == 0) or (player == 0 and bot == 2):
    print("You Win")
else:
    print("You Lose")