array = ['g', 'h', 'a', 'q', 'a', 'k', 'g', 'h']
print({arr: [ind for ind, sym in enumerate(array) if sym == arr] for arr in array})
