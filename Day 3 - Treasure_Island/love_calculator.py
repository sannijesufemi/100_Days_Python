print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

name = name1 + name2

T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")

L = name.count("l")
O = name.count("o")
V = name.count("v")

true_love = int(str(T + R + U + E) + str(L + O + V + E))

if (true_love < 10) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love >= 40) and (true_love <= 50):
    print(f"Your score is {true_love}, you are alright together")
else:
    print(f"Your score is {true_love}")




