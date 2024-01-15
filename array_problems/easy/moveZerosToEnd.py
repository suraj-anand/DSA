def moveZerosToEnd(array):
    i, j = 0, 1
    n = len(array)

    while j < n:
        if array[j] != 0 and array[i] == 0:
            array[i], array[j] = array[j], array[i]
            j += 1
            i += 1
        if array[i] != 0:
            i += 1
        else:
            j += 1

array = [1,0,1]
moveZerosToEnd(array)
print(f"post movement: {array}")