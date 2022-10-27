number_of_rooms = int(input())
total_chairs = 0
total_visitors = 0
for room in range(1, number_of_rooms + 1):
    current_room = input().split()
    chairs = current_room[0].count("X")
    visitors = int(current_room[1])
    total_chairs += chairs
    total_visitors += visitors
    if chairs < visitors:
        needed_chairs_in_room = abs(chairs - visitors)
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
if total_chairs >= total_visitors:
    total_free_chairs = abs(total_chairs - total_visitors)
    print(f"Game On, {total_free_chairs} free chairs left")


# def check_the_rooms(numbers_of_rooms):
#     total_free_chairs = 0
#     total_needed_chairs = 0
#     for room in range(1, numbers_of_rooms + 1):
#         free_chairs, visitors = input().split()
#         difference = len(free_chairs) - int(visitors)
#         if difference >= 0:
#             total_free_chairs += difference
#         else:
#             total_needed_chairs += abs(difference)
#             print(f"{abs(difference)} more chairs needed in room {room}")
#     return total_free_chairs, total_needed_chairs
#
#
# number_of_rooms = int(input())
# free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
# if free_chairs >= needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")

# number_of_rooms = int(input())
# free_chairs = 0
# enough_chairs = False
#
#
# def free_chair(chair, visitor):
#     result = abs(chair - visitor)
#     print(f"{result} more chairs needed in room {room}")
#
#
# def not_enough_chairs(chair, visitor):
#     result = chair - visitor
#     return result
#
#
# for room in range(1, number_of_rooms + 1):
#     current_room = input().split()
#     chairs = len(current_room[0])
#     visitors = int(current_room[1])
#     if chairs - visitors < 0:
#         free_chair(chairs, visitors)
#         enough_chairs = True
#     elif chairs - visitors > 0:
#         free_chairs += not_enough_chairs(chairs, visitors)
#
# if not enough_chairs:
#     print(f"Game On, {free_chairs} free chairs left")

# number_of_rooms = int(input())
# free_chairs = []
# chairs_are_enough = True
# for room in range(1, number_of_rooms + 1):
#     chairs_and_visitors = input().split()
#     current_chairs = len(chairs_and_visitors[0])
#     current_visitors = int(chairs_and_visitors[1])
#     if current_chairs >= current_visitors:
#         free_chairs.append(current_chairs - current_visitors)
#     else:
#         chairs_are_enough = False
#         needed_chairs = current_visitors - current_chairs
#         print(f"{needed_chairs} more chairs needed in room {room}")
# if chairs_are_enough:
#     print(f"Game On, {sum(free_chairs)} free chairs left")
