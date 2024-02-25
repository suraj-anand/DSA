def search(matrix, target):
    nrows = len(matrix)
    ncols = len(matrix[0])
    low = 0
    high = nrows * ncols - 1
    while low <= high:
        mid = ( low + high ) // 2
        idx = ((mid // ncols), (mid % ncols))

        if matrix[idx[0]][idx[1]] == target:
            return True
        
        elif matrix[idx[0]][idx[1]] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    r = search(matrix, target=3)
    print(r)