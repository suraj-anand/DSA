import math

def isPrime(n: int):
    end = math.floor(math.sqrt(n))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True

def isUgly(n: int) -> bool:

    for number in range(2, n+1):
        if number in (2, 3, 5):
            continue
        if isPrime(number) and n % number == 0:
            return False
    return True
        
print(isUgly(937351770))