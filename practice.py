name1=input("Enter your name: ").lower()
name2=input("Enter your crush's name: ").lower()
name=name1+name2

t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")

total1=t+r+u+e
total2=l+o+v+e

total=str(total1) + str(total2)
total_int=int(total)

if total_int<10 or total_int>90:
	print(f"Your score is {total_int},You guys go together like a coke and mentos")
elif total_int>40 and total_int<50:
	print(f"Your score is {total_int},You guys are alright together")
else:
	print(f"Your score is {total_int}")

