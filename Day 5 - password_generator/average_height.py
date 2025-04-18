student_heights = input("Input a list of student heights: ").split()

total_height = 0
counts = 0
for student in student_heights:
    total_height += int(student)
    counts += 1

average_height = round(total_height / counts)
print(average_height)