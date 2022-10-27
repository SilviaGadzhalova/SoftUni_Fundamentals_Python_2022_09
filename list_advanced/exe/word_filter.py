text = input().split()
even_length_words = [word for word in text if len(word) % 2 == 0]
print('\n'.join(even_length_words))

# words = input().split()
#
#
# def even_length(text):
#     for word in text:
#         if len(word) % 2 == 0:
#             print(word)
#
#
# even_length(words)