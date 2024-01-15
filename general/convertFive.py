def convertFive(n):
    factor = 1
    result = 0
    
    while n != 0:
        digit = n % 10
        if digit == 0:
            result = (factor * 5) + result
        else:
            result = (factor * digit) + result
        
        n //= 10
        factor *= 10
    return result
        

number = 1004
print(convertFive(number))