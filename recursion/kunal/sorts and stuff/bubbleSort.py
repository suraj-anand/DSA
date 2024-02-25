def bubble(i=0, j=1, arr=[]) -> list:
    n = len(arr)
    if i >= n-1:
        return arr
    
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

    if j >= n-1:
        return bubble(i=i+1, j=i+1, arr=arr)
    else:
        return bubble(i=i, j=j+1, arr=arr)  


    

if __name__ == "__main__":
    arr = [1, 0, 3, -1, 5000]
    arr = bubble(arr=arr)
    print(arr)
    