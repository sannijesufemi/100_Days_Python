print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1 = input().lower()
if choice1 == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice2 = input().lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue. Which colour do you choose?")
        choice3 = input().lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print  ("You fell into a hole. Game Over.")
# This is a simple text-based adventure game where the player makes choices to find treasure.
# The game has multiple endings based on the player's choices.
# The player starts at a crossroad and can choose to go left or right.
# If they go left, they encounter a lake and can choose to wait for a boat or swim across.
# If they wait, they reach an island with a house that has three doors (red, yellow, blue).
# Each door leads to a different outcome: fire, treasure, or beasts.
# If they swim, they are attacked by a trout.
# If they go right at the beginning, they fall into a hole.
# The game ends with a message indicating whether the player won or lost.
# The game uses simple conditional statements to determine the outcome based on the player's choices.
# The game is designed to be fun and engaging, with a treasure hunt theme.
# It encourages players to think critically about their choices and the consequences of those choices.
# The game can be expanded with more choices and outcomes to make it more complex and interesting.
# The game can be played multiple times with different outcomes based on the player's choices.
