def leftRotate(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1], arr[i] = arr[i], arr[i-1]
    arr[len(arr)-1] = temp

array = [1, 2, 3, 4, 5]
leftRotate(array)
print(array)