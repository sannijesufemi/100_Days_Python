student_scores = input("Input a list of student scores: ").split()

max_score = 0
student_score = 0
for score in student_scores:
    student_score = int(score)
    if student_score > max_score:
        max_score = student_score
print(f"The highest score in the class is : {max_score}")


