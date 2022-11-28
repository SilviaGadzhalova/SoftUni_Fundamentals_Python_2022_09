lines = int(input())
for line in range(lines):
    current_message = input()
    name_start, name_end = current_message.index("@"), current_message.index("|")
    age_start, age_end = current_message.index("#"), current_message.index("*")
    print(f"{current_message[name_start + 1:name_end]} is {current_message[age_start + 1:age_end]} years old.")




# lines = int(input())
# for line in range(0, lines):
#     text = input().split("|")
#     first_part = text[0]
#     name = first_part.split("@")[1]
#     second_part = text[1]
#     age = second_part.split("*")[0]
#     if "#" in age:
#         age = age.split("#")[1]
#
#     print(f"{name} is {age} years old.")
