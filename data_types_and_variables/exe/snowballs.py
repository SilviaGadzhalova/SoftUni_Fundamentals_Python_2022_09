number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for ball in range(1, number_of_snowballs+1):
    weight = int(input())
    time_needed = int(input())
    quality_of_snowball = int(input())
    snowball_value = (weight / time_needed) ** quality_of_snowball
    if snowball_value > max_value:
        max_weight = weight
        max_time = time_needed
        max_quality = quality_of_snowball
        max_value = snowball_value
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")