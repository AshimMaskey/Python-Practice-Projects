def prime_checker(number):
	if number<=0:
		print("number should not be less than or equal to zero")
	ifPrime=True
	for i in range(2,number):
		if number%i==0:
			ifPrime=False
			print("not a prime number")
			break
	if ifPrime:
		print("prime number")
n=int(input("Enter any number: "))
prime_checker(number=n)