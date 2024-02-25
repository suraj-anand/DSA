def nto1(n):
    if n <= 0:
        return
    print(n)
    nto1(n-1)

def one_to_n(n):
    if n <= 0:
        return

    one_to_n(n-1)
    print(n)

def factorial(n) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)
    
def sum_n(n) -> int:
    if n <= 1:
        return 1
    return n + sum_n(n-1)

def sum_of_digits(n, sum=0) -> int:
    if n == 0:
        return sum
    return sum_of_digits(n//10)

def sum_of_digits(n, sum=0) -> int:
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)

def prod_of_digits(n) -> int:
    if n == 0:
        return 1
    return n % 10 * prod_of_digits(n//10)

def reverse(n, rev=0):
    if n == 0:
        return rev
    rem = n % 10
    
    return reverse(n=n//10, rev=rev*10 + rem)

def palindrome(n) -> bool:
    return n == reverse(n)

def countZeros(n, count=0) -> int:
    if n == 0:
        return count
    
    rem = n % 10
    if rem == 0:
        return countZeros(abs(n//10), count=count+1)
    else:
        return countZeros(abs(n//10), count=count)
    

if __name__ == "__main__":
    print(countZeros(-12300))
        