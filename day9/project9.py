# Secret auction program
import art
bidders=[]

print(art.gavel_art)
print("Welcome to the secret auction program")

other_bidder=True

while other_bidder:
	name=input("What is your name? ")
	bid=int(input("What's your bid? "))

	bidder={}
	bidder["name"]=name
	bidder["bid"]=bid
	
	bidders.append(bidder)

	other_bidders=input("Are there other bidders? 'Yes' or 'No'? ").lower()
	if other_bidders=="no":
		other_bidder=False

highest_bid=0
highest_bidder={}

for bidder in bidders:
	if bidder["bid"]>highest_bid:
		highest_bid=bidder["bid"]
		highest_bidder=bidder

print(f'The highest bidder is {highest_bidder["name"]} at bid {highest_bidder["bid"]}.')