import re

string = input()
word = input()
pattern = fr'\b{word}\b'
result = re.findall(pattern, string, flags=re.IGNORECASE)
print(len(result))
