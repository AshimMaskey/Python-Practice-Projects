# calculator

def add(n1,n2):
	return n1+n2

def subtract(n1,n2):
	return n1-n2

def divide(n1,n2):
	return n1/n2

def multiply(n1,n2):
	return n1*n2

operations={
	"+":add,
	"*":multiply,
	"/":divide,
	"-":subtract,
	}

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number:"))

for key in operations:
	print(key)
operation_symbol=input("Which operation do you want to perform? Pick from above! ")

operation=operations[operation_symbol]
result=operation(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {result}")

user_continue=True
while user_continue:
	yes_no=input(f"Type 'y' to continue calculating with {result}, or type 'n' exit.: ").lower()
	if yes_no=="y":
		operation_symbol=input("Pick an operation: ")
		next_number=int(input("Enter the next number: "))
		operation=operations[operation_symbol]
		result1=operation(result,next_number)
		print(f"{result} {operation_symbol} {next_number} = {result1}")
		result=result1
	else:
		user_continue=False
