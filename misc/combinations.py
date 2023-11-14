def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def nCr_brute(n, r):
    nfactorial = factorial(n)
    rfactorial = factorial(r)
    n_rfactorial = factorial(n-r)

    return nfactorial / (rfactorial * n_rfactorial)

def nCr(n, r) -> int:
    result = 1
    for i in range(r):
        result = result * (n-i)
        result = result / (i+1) 
    return result

print(nCr(8, 3))