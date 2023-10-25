def printNTimes(content, n):
    if n <= 0:
        return
    print(content)
    printNTimes(content=content, n=n - 1)


printNTimes("Suraj", 5)
