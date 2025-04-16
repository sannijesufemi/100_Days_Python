row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
treasure_map = [row1, row2, row3]
print("Welcome to Treasure Island.\nYour mission is to find the treasure.") # 🚨 Don't change this text.
position = input("Where do you want to put the treasure? (Column Row)")
column = int(position[0])
row = int(position[1])

# spot = treasure_map[row - 1]
# spot[column - 1] = "X"

treasure_map [row - 1][column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")