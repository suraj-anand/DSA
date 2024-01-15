def countSort(arr):
    result = ""
    array = [0] * 26
    
    for char in arr:
        idx = ord(char) - 97
        array[idx] += 1
    
    print(array)
    for (index, num) in enumerate(array):
        if num != 0:
            result += chr(index + 97) * num
    
    return result

print(countSort("edsab"))


