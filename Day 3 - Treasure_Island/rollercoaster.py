print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
msg = ""
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill += 5
        print(f"Child tickets are ${bill}.")
    elif age<= 18:
        bill += 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a freeride on us!")
    else:
        bill += 12
        print(f"Adult tickets are ${bill}.")
    want_photo = input("Do you want a photo taken? Y / N: ")
    if want_photo == "Y":
#Add 3 dollars to the bill
        bill += 3
        print(f"Your total bill with photo is: ${bill}")
    else:
        print(f"Your total bill without photo is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

