# fruits = ["Apple", "Peach", "Pear"]
# counts = 0
# for fruit in fruits:
#     counts+= 1
#     print(f"{counts}. {fruit}")
# print("end of loop...")

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# Addition of even number between 1 and 100

sum_even = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_even += number
print(f"The sum of even number between 1 and 100: {sum_even}")
