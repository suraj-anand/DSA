def printTriangle(row, col):
    if row <= 0:
        return
    
    if col <= 0:
        printTriangle(row=row-1, col=row-1)
        print()
    else:
        printTriangle(row=row, col=col-1)
        print("*", end="")

def printTriangle2(row, col):
    if row <= 0:
        return
    
    if col <= 0:
        print()
        printTriangle2(row=row-1, col=row-1)
    else:
        print("*", end="")
        printTriangle2(row=row, col=col-1)

if __name__ == "__main__":
    row = 5
    printTriangle2(row=row, col=row)