def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [10, 100, 7, 20, 5, 6, 200, 2]
selectionSort(arr)
print(f"Sorted Array: {arr}")