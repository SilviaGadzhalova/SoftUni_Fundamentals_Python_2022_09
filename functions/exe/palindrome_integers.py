def palindrome_number(num):
        if num[0] == num[-1]:
            print("True")
        else:
            print("False")
numbers = input().split(", ")
for i in numbers:
    palindrome_number(i)

# def palindrome(number):
#     if number == number[::-1]:
#         print("True")
#     else:
#         print("False")
#
#
# numbers = list(map(str, input().split(", ")))
#
# for i in numbers:
#     palindrome(i)