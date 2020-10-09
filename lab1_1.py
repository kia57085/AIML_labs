array = ['g', 'h', 'a', 'q', 'a', 'k', 'g', 'h']
print({arr: place_list for arr in array for place_list in
    [[ind for ind, sym in enumerate(array) if sym == arr] for i in range(len(array))]})
