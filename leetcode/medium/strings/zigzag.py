def zigzag(s: str, nRows: int) -> str:
    
    rowIndex, colIndex = 0, 0
    direction = True # True - top-to-bottom, False - bottom-to-top
    matrix = [[""] * (nRows)]


    # for i in s:
    #     if rowIndex >= nRows:
    #         direction = False
        
    #     matrix[rowIndex][colIndex] = i

    #     if direction:
    #         rowIndex += 1
    #     else:
    #         colIndex += 1
    #         rowIndex -= 1
    
    print(matrix)


zigzag("PAYPALISHIRING", 5)