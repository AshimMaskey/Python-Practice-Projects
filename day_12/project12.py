# Number guessing game

GUESS_NUMBER=12

def user_guess(chance):
	user_won=False
	while chance>0 and not user_won:
		print(f"You have {chance} attempts remaining to guess the number")
		user_guess_number=int(input("Make a guess: "))
		if user_guess_number==GUESS_NUMBER:
			print(f"Correct. The num was {user_guess_number}")
			user_won=True
		elif user_guess_number>GUESS_NUMBER:
			print("too high")
		elif user_guess_number<GUESS_NUMBER:
			print("too low")
		chance-=1
	if user_won:
		print("You win")
	else:
		print("You lose")

print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100")

difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty=="easy":
	user_guess(10)
elif difficulty=="hard":
	user_guess(5)
else:
	print("Invalid choice")
