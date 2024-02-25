def binsearch(arr :list[int], target, low, high) -> int:
    if low > high:
        return -1
    
    mid = ( low + high ) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binsearch(arr, target, low, high=mid-1)

    else:
        return binsearch(arr, target, low=mid+1, high=high)

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 10, 20, 30]
    target = 20
    print(binsearch(arr, target=target, low=0, high=len(arr)-1))