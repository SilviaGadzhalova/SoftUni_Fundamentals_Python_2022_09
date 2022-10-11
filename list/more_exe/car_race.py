sequence_of_numbers = input().split()
sequence_of_numbers = [int(i) for i in sequence_of_numbers]
middle_index = int((len(sequence_of_numbers)) / 2)
left_car_time = float()
right_car_time = float()
for left_index in range(middle_index):
    current_left_time = sequence_of_numbers[left_index]
    if current_left_time == 0:
        left_car_time *= 0.80
    else:
        left_car_time += current_left_time
sequence_of_numbers.reverse()
for right_index in range(middle_index):
    current_right_time = sequence_of_numbers[right_index]
    if current_right_time == 0:
        right_car_time *= 0.80
    else:
        right_car_time += current_right_time
if left_car_time < right_car_time:
    winner = "left"
    winner_time = left_car_time
else:
    winner = "right"
    winner_time = right_car_time
print(f"The winner is {winner} with total time: {winner_time:.1f}")
