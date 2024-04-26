def merge(arr1: list, arr2: list) -> list:
    arr3 = []
    left, right = 0, 0
    m, n = len(arr1), len(arr2)
    
    while left < m and right < n:
        if arr1[left] < arr2[right]:
            arr3.append(arr1[left])
            left += 1
        else:
            arr3.append(arr2[right])
            right += 1
            
    
    while left < m:
        arr3.append(arr1[left])
        left += 1
    
    while right < n:
        arr3.append(arr2[right])
        right += 1
    
    return arr3
        

def mergeSort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[0: mid])
    right = mergeSort(arr[mid: ])
    return merge(left, right)

if __name__ == "__main__":
    arr = [10, 9, 5, 4, 1]
    arr = mergeSort(arr)
    print(arr)