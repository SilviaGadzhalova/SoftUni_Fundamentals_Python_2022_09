group_size = int(input())
days = int(input())
day_points = 0
for day in range(1,days+1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        day_points -= 3*group_size
    if day % 5 == 0:
        day_points += 20*group_size
        if day % 3 == 0:
            day_points -= 2 * group_size
    day_points += 50 - (2 * group_size)
companions_point = int(day_points//group_size)
print(f"{group_size} companions received {companions_point} coins each.")

