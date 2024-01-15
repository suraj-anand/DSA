def rotate90(matrix):
    n = len(matrix)
    return matrix

def transpose(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n-2):
        for j in range(n):
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
    return matrix

def prettyMatrix(matrix):
    n,m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(f"{matrix[i][j]}", end="\t")
        print('')
    print("----------------")

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(f"Original Matrix:")
prettyMatrix(matrix)

print("Transposed Matrix:")
prettyMatrix(transpose(matrix=matrix))