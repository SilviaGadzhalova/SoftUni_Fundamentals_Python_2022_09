first_line = input().split(", ")
second_line = input().split(", ")
iteration_strings = []
for first_word in first_line:
    for second_word in second_line:
        if first_word in second_word:
            iteration_strings.append(first_word)
            break
print(iteration_strings)

# 1.1
# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]
# print(substrings)