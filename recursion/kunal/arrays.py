def isSorted(arr, index=0) -> bool:
    if index >= len(arr) - 2:
        return True
    
    currentComparsion = arr[index] < arr[index + 1]
    return currentComparsion and isSorted(arr, index=index+1)

def lsearch(arr, target, index=0) -> bool:
    if index >= len(arr):
        return False
    present = arr[index] == target
    return present or lsearch(arr, target, index=index+1)

def lsearch_indices(arr, target, index=0) -> list:
    result = []
    if index >= len(arr):
        return result
    
    if arr[index] == target:
        result.append(index)

    r = lsearch_indices(arr, target, index=index+1)
    for i in r:
        result.append(i)
    return result

if __name__ == "__main__":
    arr = [1, 3, 5, 4, 5, 6, 7]
    # print(isSorted(arr))
    print(lsearch_indices(arr, target=5))