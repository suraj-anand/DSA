def findComplement(n):
    revBinary = []
    
    while n != 0:
        if n % 2 == 0:
            revBinary.append(1)
        else:
            revBinary.append(0) 
        n //= 2
    
    r = 0
    twoPower = 0
    for i in revBinary:
        r += (i * 2 ** twoPower)
        twoPower += 1
    return r

if __name__ == "__main__":
    n = 5
    print(findComplement(n))