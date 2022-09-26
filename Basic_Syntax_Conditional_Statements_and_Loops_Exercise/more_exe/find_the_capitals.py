from string import ascii_uppercase

string = input()
output = list()

for i in range(len(string)):
    for j in ascii_uppercase:
        if j in string[i]:
            output.append(i)
            break

print(output)

# string = input()
# final_list = []
# for i in range(len(string)):
#     current_letter = string[i]
#     if 65 <= ord(current_letter) <= 90:
#         final_list.append(i)
# print(final_list)