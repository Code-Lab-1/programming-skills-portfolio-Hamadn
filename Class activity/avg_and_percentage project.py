from ast import MatchSequence


subject_1 = "Maths"
subject_2 = "English"
subject_3 = "Physics"
subject_4 = "Computing"
subject_5 = "Chemistry"

name = input("Enter your name:\n")
maths_marks = int(input("Enter your marks for Maths:\n"))
english_marks = int(input("Enter your marks for English:\n"))
physics_marks = int(input("Enter your marks for Physics:\n"))
computing_marks = int(input("Enter your marks for Computing:\n"))
chemistry_marks = int(input("Enter your marks for Chemistry:\n"))

total = 500
marks_obtained = maths_marks + english_marks + physics_marks + computing_marks + chemistry_marks
average = marks_obtained / 5
per_maths = (maths_marks / total)*100
per_english = (english_marks / total)*100
per_physics = (physics_marks / total)*100
per_computing = (computing_marks / total)*100
per_chemistry = (chemistry_marks / total)*100

print(name)
print("Your average marks are:" , average)
print("Percentage for Maths:" , per_maths)
print("Percentage for English:" , per_english)
print("Percentage for Physics:" , per_physics)
print("Percentage for Computing:" , per_computing)
print("Percentage for Chemistry:" , per_chemistry)