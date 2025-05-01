print("╔════════════════════╗")
print("║ 💎     TREASURE     💎 ║")
print("║                    ║")
print("║   🔐  Locked Box   🔐   ║")
print("║                    ║")
print("╚════════════════════╝")

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction=input("You are at crossroad. Choose between:- left and right: ")

if direction=="left":
	swim_wait=input("You come to a lake. There is a island in the middle of the lake. Do you want to swim or wait? ")
	if swim_wait=="swim":
		door=input("You arrive at island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you want to choose? ")
		if door=="blue":
			print("You win")
		else:
			print("Game Over")
	else:
		print("Game Over")
else:
	print("Game Over")