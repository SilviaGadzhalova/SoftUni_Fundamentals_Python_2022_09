people = int(input())
current_lift = [int(num) for num in input().split(' ')]

for lift in range(len(current_lift)):
    while current_lift[lift] < 4 and people > 0:
        current_lift[lift] += 1
        people -= 1

total_lift_size = len(current_lift) * 4
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif total_lift_size > sum(current_lift):
    print("The lift has empty spots!")
print(*current_lift, sep=' ')
