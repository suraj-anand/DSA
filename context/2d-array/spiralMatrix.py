def spiralMatrix(matrix: list):
    result = []
    
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result = []

    while left <= right and top <= bottom:
        print(f"top = {top}, bottom = {bottom}, left = {left}, right = {right}")
        
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        print(result)
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        print(result)

        if left != right:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
        print(result)
    
    return result

            
       
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = spiralMatrix(matrix)
print(result)
