string = input().split()
reversed_list = []
for element in string:
    if  int(element) > 0:
        new_element = - int(element)
        reversed_list.append(new_element)
    else:
        new_element = abs(int(element))
        reversed_list.append(new_element)
print(reversed_list)

# list_of_numbers = input().split()
# opposite_numbers = []
# for element in list_of_numbers:
#     current_number = -int(element)
#     opposite_numbers.append(current_number)
# print(opposite_numbers)