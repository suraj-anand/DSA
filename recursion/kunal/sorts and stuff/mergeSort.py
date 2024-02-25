import sys
sys.setrecursionlimit(10)

def merge(arr1, arr2):
    result = []
    
    left, right = 0, 0
    m, n = len(arr1), len(arr2)

    while left < m and right < n:
        if arr1[left] < arr2[right]:
            result.append(arr1[left])
            left += 1
        else:
            result.append(arr2[right])
            right += 1
    
    while left < m:
        result.append(arr1[left])
        left += 1
    
    while right < n:
        result.append(arr2[right])
        right += 1

def merge_sort(arr) -> list:
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n // 2
    left_arr = merge_sort(arr=arr[0:mid])
    print(left_arr)
    right_arr = merge_sort(arr=arr[mid: n])
    print(right_arr)
    return merge(arr1=left_arr, arr2=right_arr)
if __name__ == "__main__":
    arr = [5,4,3,2,1]
    arr = merge_sort(arr=arr)
    