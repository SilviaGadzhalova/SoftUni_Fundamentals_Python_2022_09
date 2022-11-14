courses = {}
while True:
    current_string = input()
    if current_string == "end":
        break
    current_course, student = current_string.split(" : ")
    if current_course not in courses.keys():
        courses[current_course] = []
    courses[current_course].append(student)
for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
