number_of_people = int(input())
lift_starting_stage = input().split()
lift = []
current_people = number_of_people
total_lift = len(lift_starting_stage) * 4
for spot in lift_starting_stage:
    spot = int(spot)
    if current_people == 0:
        spot += current_people
        lift.append(str(spot))
        break
    if current_people < 4:
        spot += current_people
        lift.append(str(spot))
        current_people -= spot
    if spot == 0:
        spot += 4
        lift.append(str(spot))
        current_people -= 4
    elif spot != 0 and current_people != 0:
        current_people -= (4 - spot)
        spot += 4 - spot
        lift.append(str(spot))

if total_lift > number_of_people:
    print("The lift has empty spots!")
elif number_of_people > current_people:
    print(f"There isn't enough space! {abs(current_people)} people in a queue!")
print(" ".join(lift))

# number_of_people = int(input())
# lift_starting_stage = input().split()
# lift = []
# current_people = number_of_people
# for spot in lift_starting_stage:
#     spot = int(spot)
#     if current_people < 4:
#         spot += current_people
#         lift.append(str(spot))
#         current_people -= spot
#     if spot == 0:
#         spot += 4
#         lift.append(str(spot))
#         current_people -= 4
#     elif spot != 0 and current_people != 0:
#         current_people -= (4 - spot)
#         spot += 4 - spot
#         lift.append(str(spot))
#
#
# if number_of_people < 16:
#     print("The lift has empty spots!")
# else:
#     print(f"There isn't enough space! {current_people} people in a queue!")
# print(" ".join(lift))
