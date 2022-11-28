import re

string = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
result = re.findall(pattern, string)
print(','.join(result))
