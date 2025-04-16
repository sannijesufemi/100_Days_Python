import random

rock = '''
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
   Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to the famous Rock, Paper, Scissors Game.")
user_play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
play_list = [rock, paper, scissors]
play_length = len(play_list)
computer_play = random.randint(0, play_length - 1)

if user_play == 0 and computer_play == 2:
    print("You chose:")
    print(f"{play_list[user_play]}")
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("You win! 🫡")
elif user_play == 2 and computer_play == 0:
    print("You chose:")
    print(f"{play_list[user_play]}")
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("You lose! 😔")
elif user_play == 2 and computer_play == 1:
    print("You chose:")
    print(f"{play_list[user_play]}")
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("You win! 🫡")
elif user_play == 1 and computer_play == 2:
    print("You chose:")
    print(f"{play_list[user_play]}")
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("You lose! 😔")
elif user_play == 1 and computer_play == 0:
    print("You chose:")
    print(f"{play_list[user_play]}")
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("You win! 🫡")
elif user_play == 0 and computer_play == 1:
    print("You chose:")
    print(f"{play_list[user_play]}")
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("You lose! 😔")
elif user_play == computer_play:
    print("You chose:")
    print(f"{play_list[user_play]}")
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("It\'s a Draw! 🤝")
else:
    print("Computer chose:")
    print(f"{play_list[computer_play]}")
    print("You typed an invalid number, You lose!")
