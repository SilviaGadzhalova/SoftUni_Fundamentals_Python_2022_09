import re

dates = input()
search_pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"
result = re.findall(search_pattern, dates)
#result = re.finditer(search_pattern, dates)
for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}", )
    #print(f"Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}", )