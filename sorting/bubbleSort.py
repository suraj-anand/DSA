def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(1, n-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = [10, 100, 7, 20, 5, 6, 200, 2]
bubbleSort(arr)
print(f"Sorted Array: {arr}")
