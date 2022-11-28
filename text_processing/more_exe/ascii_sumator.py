first_char = ord(input())
second_char = ord(input())
sum_of_characters = 0

for character in input():
    if first_char < ord(character) < second_char:
        sum_of_characters += ord(character)

print(sum_of_characters)
