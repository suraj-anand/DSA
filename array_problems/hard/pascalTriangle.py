def nCr(n, r):
    result = 1
    for i in range(r):
        result = result * (n-i)
        result = result // (i+1)
    return result

def generatePascalTriangle(row):
    result = []
    for i in range(1, row+1):
        row_list = []
        for j in range(1, i+1):
            row_list.append(nCr(i-1, j-1))
        result.append(row_list)
    return result
        
print(
    generatePascalTriangle(10)
)