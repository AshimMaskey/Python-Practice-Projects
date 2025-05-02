# Rock, Paper and Scissors

import random
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''


user_input=int(input("Enter your choice: 0 for rock, 1 for paper and 2 for scissors: "))

game_images=[rock,paper,scissors]
print(game_images[user_input])

random_number=random.randint(0,2)

print("Computers choice:")
print(game_images[random_number])

if user_input==random_number:
	print("Draw")
elif user_input>=3 or user_input<0:
	print("Invalid input!")
elif user_input==0 and random_number==2:
	print("you win")
elif user_input==1 and random_number==0:
	print("you win")
elif user_input==2 and random_number==1:
	print("you win")
else:
	print("computer wins, you are bot lol")
