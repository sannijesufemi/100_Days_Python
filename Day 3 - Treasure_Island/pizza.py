print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")

bill = 0

if size == "S":
    bill += 15
    add_pepperoni = input("Do you want pepperoni? Y or N? ")
    if add_pepperoni == "Y":
        bill += 2
    else:
        bill += 0
    extra_cheese = input("Do you want extra cheese? Y or N? ")
    if extra_cheese == "Y":
        bill += 1
    else:
        bill += 0
elif size == "M":
    bill += 20
    add_pepperoni = input("Do you want pepperoni? Y or N? ")
    if add_pepperoni == "Y":
        bill += 3
    else:
        bill += 0
    extra_cheese = input("Do you want extra cheese? Y or N? ")
    if extra_cheese == "Y":
        bill += 1
    else:
        bill += 0
elif size == "L":
    bill += 25
    add_pepperoni = input("Do you want pepperoni? Y or N? ")
    if add_pepperoni == "Y":
        bill += 3
    else:
        bill += 0
    extra_cheese = input("Do you want extra cheese? Y or N? ")
    if extra_cheese == "Y":
        bill += 1
    else:
        bill += 0
else:
    print("Invalid pizza size")
print(f"Your final bill is: ${bill}")