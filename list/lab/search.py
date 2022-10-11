n = int(input())
word = input()
lst = []
lst_word = []
for _ in range(n):
    current_str = input()
    lst.append(current_str)
    if word in current_str:
        lst_word.append(current_str)
print(lst)
print(lst_word)
# for i in range(len(lst)-1, -1, -1):
#     element = lst[i]
#     if word not in element:
#         lst.remove(element)

