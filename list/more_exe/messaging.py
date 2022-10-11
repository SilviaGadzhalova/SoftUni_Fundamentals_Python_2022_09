sequence_of_numbers = input().split()
string = input()
indices_list = []
final_message = ""
for index in range(len(sequence_of_numbers)):
    current_combination = sequence_of_numbers[index]
    current_sum = 0
    for sequence in range(len(current_combination)):
        current_sum += int(current_combination[sequence])
    indices_list.append(current_sum)
message_indices_count = len(string)
for symbol in range(len(sequence_of_numbers)):
    current_index = indices_list[symbol]
    while current_index > (message_indices_count - 1):
        current_index -= message_indices_count
    current_symbol = string[current_index]
    string = string[:current_index] + string[current_index + 1::]
    final_message += current_symbol
print(final_message)