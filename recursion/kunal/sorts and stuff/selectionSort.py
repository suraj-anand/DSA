def selection(i=0, j=0, minIndex=0, arr=[]):
    n = len(arr)
    if i >= n-1:
        return arr
    
    if j >= n:
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return selection(i=i+1, j=i+1, minIndex=i+1, arr=arr)
    else:
        if arr[j] < arr[minIndex]:
            minIndex = j
        return selection(i=i, j=j+1, minIndex=minIndex, arr=arr)

if __name__ == "__main__":
    arr = [1, 0, 3, -1, 5000]
    arr = selection(arr=arr)
    print(arr)