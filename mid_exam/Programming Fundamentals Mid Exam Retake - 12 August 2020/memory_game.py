sequence_of_elements = input().split()
total_moves = 0
while True:
    command = input()
    if command == "end":
        break

    total_moves += 1
    split_command = list(map(int,command.split()))
    index1 = split_command[0]
    index2 = split_command[1]

    if index1 == index2 or index1 < 0 or index2 < 0 or (len(sequence_of_elements) - 1) < index1 or (len(sequence_of_elements) - 1) < index2:
        print("Invalid input! Adding additional elements to the board")
        insert_index = int(len(sequence_of_elements) / 2)
        insert_element = f'-{total_moves}a'
        sequence_of_elements.insert(insert_index, insert_element)
        sequence_of_elements.insert(insert_index, insert_element)
    elif sequence_of_elements[index1] == sequence_of_elements[index2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index1]}!")
        sequence_of_elements.remove(sequence_of_elements.pop(index1))
    elif sequence_of_elements[index1] != sequence_of_elements[index2]:
        print("Try again!")

    if len(sequence_of_elements) == 0:
        break

if len(sequence_of_elements) == 0:
    print(f"You have won in {total_moves} turns!")
else:
    print("Sorry you lose :(")
    print(*sequence_of_elements, sep=' ')
