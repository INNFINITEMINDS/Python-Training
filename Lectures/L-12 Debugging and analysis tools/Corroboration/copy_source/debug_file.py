from itertools import permutations

items = range(1, 6)

choices = permutations(items,6)

current = 0


for ordinal, item in enumerate(choices,1):
    if item[0] == current:
        continue
    print(item)
    current = item[0]