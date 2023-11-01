def linearSearch(array, key):
    for (index, element) in enumerate(array):
        if element == key:
            return index
    return -1

array = [10, 20, 30, 40, 50]
print(linearSearch(array, 30))
print(linearSearch(array, 300))
