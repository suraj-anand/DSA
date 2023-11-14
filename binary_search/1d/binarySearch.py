# Iterative Approach
def binarySearch(arr, target):
    low  = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1

# Recursive Approach
def binarySearch(arr, target, low, high):
    # Base Condition
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binarySearch(arr, target=target, low=low, high=mid-1)

    else:
        return binarySearch(arr, target=target, low=mid+1, high=high)
    
arr = [10, 20, 30, 40, 50, 60]
print(binarySearch(arr, target=100, low=0, high=len(arr)-1))