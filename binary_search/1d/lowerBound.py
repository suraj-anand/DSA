def linearLowerBound(arr, x):
    for (index, element) in enumerate(arr):
        if element >= x:
            return index
    return len(arr)

def lowerBound(arr, x):
    low, high = 0, len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        elif arr[mid] < x:
            high = mid - 1
    return ans
            
if __name__ == "__main__":
    arr = [1,2,2,3,3,5]
    x = 
    print(lowerBound(arr=arr, x=x))