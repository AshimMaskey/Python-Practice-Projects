# Tip calculator
print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_numbers=int(input("How many people to split the bill? "))

total_bill+=(tip_percentage/100)*total_bill
splitted_amount=round(total_bill/people_numbers,2)

print(f"Each person should pay: ${splitted_amount:.2f}")