# HangMan Project

import random
word_list=["naruto", "hamburger", "brush"]
hangman_stages =hangman_stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]


choosen_word=random.choice(word_list)
print(f"the solution is {choosen_word}")

display=[]
for _ in range(len(choosen_word)):
	display.append("_")
print(display)

end_of_game=False
lives=7
while not end_of_game:
	guess=input("Enter your guess: ").lower()

	for position in range(len(choosen_word)):
		if choosen_word[position]==guess:
			display[position]=guess
	if "_" not in display:
		end_of_game=True
		print("You win")
	
	if guess not in choosen_word:
		print(hangman_stages[lives-1])
		lives-=1
		
	if lives==0:
		print("you lose")
		end_of_game=True

	print(display)

