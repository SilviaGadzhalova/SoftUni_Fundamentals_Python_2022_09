import re

participants = input().split(", ")
command = input()
participants_dict = {}
while command != "end of race":
    name_pattern = r'[A-Za-z]'
    name_match = re.findall(name_pattern, command, flags=re.IGNORECASE)
    digits_pattern = r'[0-9]'
    run_time_list = re.findall(digits_pattern, command)
    name = "".join(name_match)
    distance = sum([int(x) for x in run_time_list])
    if name in participants:
        if name not in participants_dict:
            participants_dict[name] = distance
        else:
            participants_dict[name] += distance
    command = input()
sorted_results = dict(sorted(participants_dict.items(), key=lambda x: -x[1]))
rank = 0
for name in sorted_results:
    rank += 1
    if rank > 3:
        break
    if rank == 1:
        current_rank = "1st"
    elif rank == 2:
        current_rank = "2nd"
    elif rank == 3:
        current_rank = "3rd"
    print(f"{current_rank} place: {name}")

