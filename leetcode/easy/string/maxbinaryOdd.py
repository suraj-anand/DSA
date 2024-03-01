def maximumOddBinaryNumber(s: str) -> str:
    n = len(s)
    countOnes = 0
    for i in s:
        if i == '1':
            countOnes += 1
    r = [0] * n
    r[-1] = 1
    countOnes -= 1
    
    for idx in range(countOnes):
        r[idx] = 1
    
    return "".join(list(map(str, r)))
    
    
if __name__ == "__main__":
    s = "0101"
    r = maximumOddBinaryNumber(s)
    print(r)