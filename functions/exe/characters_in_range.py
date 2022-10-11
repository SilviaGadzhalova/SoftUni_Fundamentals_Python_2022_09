def character_between_two(first, second):
    characters = []
    for current_char in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_char))
    return characters


first_char = input()
second_char = input()
result = character_between_two(first_char, second_char)
print(" ".join(result))
# print(*result)
# print(*result, sep= " ")
