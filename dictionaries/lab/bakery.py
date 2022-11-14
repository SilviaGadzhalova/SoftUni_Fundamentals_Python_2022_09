items = input().split()
bakery = {}
for index in range(0, len(items), 2):
    bakery[items[index]] = int(items[index + 1])
    # key = items[index]
    # value = int(items[index + 1])
    # bakery[key] = value
print(bakery)
