from math import floor


def coordinate_system(arg1, arg2):
    if arg1 <= arg2:
        return f"({x1}, {x2})"
    elif arg2 <= arg1:
        return f"({y1}, {y2})"


x1 = floor(float(input()))
x2 = floor(float(input()))
y1 = floor(float(input()))
y2 = floor(float(input()))

sum_x = floor(abs(x1) + abs(x2))
sum_y = floor(abs(y1) + abs(y2))

print(coordinate_system(sum_x, sum_y))
