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
print("You Chose:")

if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)
else:
    print("Invalid Number")

bot = random.randint(0, 2)
print("Computer Chose:")

if bot == 0:
    print(rock)
elif bot == 1:
    print(paper)
else:
    print(scissors)

if 2 < player < 0:
    print("Invalid Number")
elif player == 2 and bot == 0:
    print("You Lose")
elif player == 0 and bot == 2:
    print("You Win")
elif player > bot:
    print("You Win")
elif player < bot:
    print("You Lose")
elif player == bot:
    print("You Draw")