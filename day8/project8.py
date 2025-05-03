# Encryption project

import alphabet
alphabets=alphabet.alphabet
print(len(alphabets))

def encode():
	text=input("Type your message:\n").lower()
	shift=int(input("Shift Number:"))
	encrypted_text=""

	for char in text:
		index=alphabets.index(char)
		new_index=index+shift
		if new_index<26:
			encrypted_text+=alphabets[new_index]
		else:
			new_index=new_index%26
			encrypted_text+=alphabets[new_index]
	print(f"The decoded text is {encrypted_text}")

def decode():
	text=input("Type your message:\n").lower()
	shift=int(input("Shift Number:"))
	decrypted_text=""

	for char in text:
		index=alphabets.index(char)
		new_index=index-shift
		decrypted_text+=alphabets[new_index]
	print(f"The encoded text is {decrypted_text}")

user_exit=False
while user_exit==False:
	direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ")
	if direction=="encode":
		encode()
	elif direction=="decode":
		decode()
	else:
		print("Invalid input")
	
	user_input=input("Do you want to exit or continue? Type 'exit' or 'continue'? ").lower()
	if user_input=="exit":
		user_exit=True