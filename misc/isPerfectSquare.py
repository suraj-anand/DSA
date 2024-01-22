def isPerfectSquare(num):
    low, high = 1, num
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid == (num // mid):
            return True

        elif mid > (num // mid):
            high = mid - 1
        
        else:
            low = mid + 1
    return False

n = int(input("Enter a number: "))
print(n, isPerfectSquare(n))