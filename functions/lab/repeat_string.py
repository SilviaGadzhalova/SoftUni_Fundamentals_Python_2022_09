# def repeat_string(current_string, num):
#     return current_string*num
#
# string = input()
# number = int(input())
# print(repeat_string(string, number))
string = input()
number = int(input())
result = lambda string, num: string * num
print(result(string, number))
