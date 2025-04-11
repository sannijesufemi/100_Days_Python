print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentage_tip = ((tip / 100) * total_bill)

bill_per_person = int(input("How many people to split the bill? "))
total_bill += percentage_tip
bill = total_bill / bill_per_person

print(f"Each person should pay: ${bill:.2f}")

# another way is to use the round function,
# But in a situation whereby the answer is 33.60,
# round will output 33.6 while fstring formatting will give 33.60
final_bill = round(bill, 2)
print(f"Each person pays: ${final_bill}")