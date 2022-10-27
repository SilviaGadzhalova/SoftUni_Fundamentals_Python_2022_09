def multiplication_sign(arg1, arg2, arg3):
    if (arg1 > 0 and arg2 > 0 and arg3 > 0) or \
            (arg1 > 0 and arg2 < 0 and arg3 < 0) or \
            (arg2 > 0 and arg1 < 0 and arg3 < 0) or \
            (arg3 > 0 and arg1 < 0 and arg2 < 0):
        print("positive")
    elif arg1 == 0 or arg2 == 0 or arg3 == 0:
        print("zero")
    elif arg1 < 0 or arg2 < 0 or arg3 < 0:
        print("negative")


first_number = int(input())
second_number = int(input())
third_number = int(input())
multiplication_sign(first_number, second_number, third_number)
