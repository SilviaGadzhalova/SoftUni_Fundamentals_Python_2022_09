version_number = [int(number) for number in input().split(".")]


def new_version(current_version):
    first_number = current_version[0]
    second_number = current_version[1]
    third_number = current_version[2]

    if third_number == 9:
        third_number = 0
        if second_number == 9:
            second_number = 0
            first_number += 1
            if first_number > 9:
                first_number = 0
        elif second_number < 9:
            second_number += 1

    elif third_number < 9:
        third_number += 1

    return print(f"{first_number}.{second_number}.{third_number}")


# new_version(version_number)
#
# version = [int(number) for number in input().split(".")]
# version[-1] += 1
# for index in range(len(version) - 1, -1, -1):
#     if version[index] > 9:
#         version[index] = 0
#         if index - 1 >= 0:
#             version[index - 1] += 1
# print('.'.join(str(number) for number in version))


# current_version = input().split(".")
# version = current_version[0] + current_version[1] + current_version[2]
# new_version = int(version) + 1
# new_version_lst = [digit for digit in str(new_version)]
# print(".".join(new_version_lst))