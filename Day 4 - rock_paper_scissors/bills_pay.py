import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_count = len(names)
payee = random.randint(0, name_count - 1)
print(payee)
print(f"{names[payee]}, is going to buy the meal today!")