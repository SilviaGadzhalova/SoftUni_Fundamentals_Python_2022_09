import re

valid_urls = []
pattern = '(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
text = input()
while text:
    result = re.search(pattern, text)
    if result:
        valid_urls.append(result.group(0))
    text = input()
for valid_url in valid_urls:
    print(valid_url)