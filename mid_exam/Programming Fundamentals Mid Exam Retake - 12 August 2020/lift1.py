people = int(input())
current_people = people
current_lift_state = [int(num) for num in input().split()]
new_lift_state = []
total_people = len(current_lift_state)*4
for x in current_lift_state:
    if current_people < 4:
        new_lift_state.append(current_people)
        print("The lift has empty spots!")
        print(*new_lift_state, sep=' ')
        break
    if x == 0:
        x += 4
        current_people -= 4
        new_lift_state.append(x)
    else:
        current_people += x
        x = x+(4-x)
        current_people -= 4
        new_lift_state.append(x)

if people > total_people:
    difference = abs(people - current_people)
    print(f"There isn't enough space! {difference} people in a queue!")
    print(*new_lift_state, sep=' ')
