tasks = []
while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("-")
    priority = int(split_command[0])
    name_of_task = split_command[1]
    tasks.append([priority, name_of_task])
sorted_tasks = [tasks_data[1] for tasks_data in sorted(tasks)]
print(sorted_tasks)