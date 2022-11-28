# string = input().split()
# new_string = []
# for word in string:
#     new_string.append(word*len(word))
# print(''.join(new_string))
[print(s*len(s), end="") for s in input().split()]