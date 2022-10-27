sequence = [int(number) for number in input().split()]
removed_pokemons = []
while len(sequence) > 0:
    current_index = int(input())
    if current_index < 0:
        removed = sequence[0]
        sequence[0] = sequence[-1]
    elif current_index >= len(sequence):
        removed = sequence[-1]
        sequence[-1] = sequence[0]
    else:
        removed = sequence.pop(current_index)
    removed_pokemons.append(removed)
    result_list = []
    for number in sequence:
        if number <= removed:
            result_list.append(number + removed)
        else:
            result_list.append(number - removed)
    sequence = result_list.copy()
print(sum(removed_pokemons))