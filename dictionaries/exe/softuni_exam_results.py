exam_results = {"Results": {}, "Submissions": {}}
command = input()
while command != "exam finished":
    command = command.split("-")
    if len(command) == 2:
        user_name = command[0]
        for language in exam_results["Results"]:
            for name in exam_results["Results"][language]:
                if name == user_name:
                    del exam_results["Results"][language][name]
                    break
    else:
        user_name, language, points = command[0], command[1], command[2]
        points = int(points)
        if language not in exam_results["Results"]:
            exam_results["Results"][language] = {user_name: points}
            exam_results["Submissions"][language] = 1
        elif language in exam_results["Results"]:
            exam_results["Submissions"][language] += 1
            if user_name not in exam_results["Results"][language]:
                exam_results["Results"][language][user_name] = points
            else:
                if points > exam_results["Results"][language][user_name]:
                    exam_results["Results"][language][user_name] = points
    command = input()
print("Results:")
for language in exam_results["Results"]:
    for username in exam_results["Results"][language]:
        print(f"{username} | {exam_results['Results'][language][username]}")
print("Submissions:")
for language in exam_results["Submissions"]:
    print(f"{language} - {exam_results['Submissions'][language]}")
