def removeChars (string1, string2):
    array = [0] * 26

    for i in string2:
        index = ord(i) - 97
        array[index] += 1
    
    result = ""
    for i in string1:
        index = ord(i) - 97
        if array[index] == 0:
            result += i

    return result

print(
    removeChars("cat", "c")
)
