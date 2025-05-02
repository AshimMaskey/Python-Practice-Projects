# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator Project")

nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like in your password?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))

password=[]

for i in range(nr_letters):
	random1=random.randint(0, len(letters)-1)
	password.append(letters[random1])

for i in range(nr_symbols):
	random1=random.randint(0, len(symbols)-1)
	password.append(symbols[random1])

for i in range(nr_numbers):
	random1=random.randint(0, len(numbers)-1)
	password.append(numbers[random1])

random.shuffle(password)

string_pass=""

for char in password:
	string_pass+=char

print(string_pass)