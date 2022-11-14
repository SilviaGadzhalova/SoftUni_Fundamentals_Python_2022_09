pairs = int(input())
students_grades_dictionary = {}
grade_counter = 0
for student in range(0, pairs):
    current_student = input()
    current_grade = float(input())
    if current_student not in students_grades_dictionary.keys():
        students_grades_dictionary[current_student] = []
    students_grades_dictionary[current_student].append(current_grade)

for student, grade in students_grades_dictionary.items():
    final_grade = sum(grade)/len(grade)
    if final_grade >= 4.5:
        print(f"{student} -> {final_grade:.2f}")
