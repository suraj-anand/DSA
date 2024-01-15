def transitionPoint(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if (arr[mid] == 1 and arr[mid - 1] == 0) or (arr[mid] == 1 and (mid - 1) == -1):
            return mid
        elif arr[mid] == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(transitionPoint([0, 0, 0, 0, 1, 1]))