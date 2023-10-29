def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

arr = [10, 100, 7, 20, 5, 6, 200, 2]
insertionSort(arr)
print(f"Sorted Array: {arr}")