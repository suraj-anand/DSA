def pow(x, n):
    
    if n > 0:
        result = 1
        while n != 0:
            result *= x
            n -= 1
        return round(result, 5)
    
    elif n == 0:
        return x
    
    else:
        result = 1
        while n != 0:
            result *= x
            n += 1
        print(result)
        return round(1 / result, 5)
            

print(pow(0.00001, 2147483647))
    