def getLeaders(arr: list):
    max = -1
    result = []

    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max:
            result.append(arr[i])
            max = arr[i]
    result.reverse()
    return result 

arr = [16,17,4,3,5,2]
print(getLeaders(arr))