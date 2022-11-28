numbers = [int(element) for element in input().split()]
text = input()

while text != "find":
    text = list(text)
    i_numbers = 0
    started = False
    type_treasure = []
    location = []

    for i_text in range(len(text)):
        current_letter = ord(text[i_text])
        current_letter -= numbers[i_numbers]
        text[i_text] = chr(current_letter)
        i_numbers += 1
        if i_numbers == len(numbers):
            i_numbers = 0

    for element in text:
        if element == '&' and started:
            started = False
        elif element == '&':
            started = True
        elif started:
            type_treasure.append(element)

    for element in text:
        if element == "<":
            started = True
        elif element == ">":
            started = False
        elif started:
            location.append(element)

    print(f"Found {''.join(type_treasure)} at {''.join(location)}")
    text = input()