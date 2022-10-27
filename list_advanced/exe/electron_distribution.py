number_of_electrons = int(input())
list_of_electrons = []
start_electrons = number_of_electrons
position = 0
while start_electrons > 0:
    position += 1
    current_position = 2 * position * position
    if sum(list_of_electrons) + current_position <= number_of_electrons:
        list_of_electrons.append(current_position)
        start_electrons -= current_position
    else:
        list_of_electrons.append(start_electrons)
        break

print(list_of_electrons)

# number_of_electrons = int(input())
# list_of_electrons = []
#
# for position in range(1, number_of_electrons + 1):
#     current_position = 2 * position * position
#     number_of_electrons -= current_position
#     list_of_electrons.append(current_position)
#     if number_of_electrons - current_position <= 0:
#         break
# if number_of_electrons > 0:
#     list_of_electrons.append(number_of_electrons)
# print(list_of_electrons)


# number = int(input())
# n = 1
# lst = []
# while number > 0:
#     electron = 2*n**2
#     lst.append(min(number, electron))
#     number -= lst[-1]
#     n += 1
#
# print(lst)


# electrons = int(input())
# list_with_filled_shells = []
#
# for electron in range(1, electrons + 1):
#     result = 2 * (electron ** 2)
#     if result > electrons:
#         list_with_filled_shells.append(electrons)
#         electrons -= electrons
#         break
#     electrons -= result
#     list_with_filled_shells.append(result)
#     if electrons <= 0:
#         break
#
# print(list_with_filled_shells)