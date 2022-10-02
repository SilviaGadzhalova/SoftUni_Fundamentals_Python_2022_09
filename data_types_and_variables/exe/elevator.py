# from math import ceil
#
# number_of_people = int(input())
# elevator_capacity = int(input())
# number_of_courses = ceil(number_of_people / elevator_capacity)
# print(number_of_courses)

number_of_people = int(input())
elevator_capacity = int(input())
number_of_courses = number_of_people // elevator_capacity
if number_of_people % elevator_capacity != 0:
    number_of_courses +=1
print(number_of_courses)