array = ['g', 'h', 'a', 'q', 'a', 'k', 'g', 'h']

place = dict()

for i, sym in enumerate(array):
    if sym in place:
        place[sym].append(i)
    else:
        place[sym] = [i]

print(place)
