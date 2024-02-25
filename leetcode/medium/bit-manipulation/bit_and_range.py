MAX_BITS = 32

def toBinary(n: int) -> int:
    bits = [0] * MAX_BITS
    result = []
    while n != 0:
        result.append(n%2)
        n //= 2

    ridx = len(result) - 1
    bidx = MAX_BITS - len(result)
    while ridx > -1:
        bits[bidx] = result[ridx]
        bidx += 1
        ridx -= 1
        
    return bits

def toDecimal(arr: list) -> int:
    idx = len(arr) - 1
    factor = 0
    result = 0
    while idx > -1:
        if arr[idx] == 1:
            result += 2 ** factor
        arr[idx]
        factor += 1
        idx -= 1
    return result

def rangeBitwiseAnd(left: int, right: int) -> int:
    first = toBinary(left)
    second = toBinary(right)
    result_bits = [0] * MAX_BITS
    
    index = 0
    while index < MAX_BITS:
        if first[index] == second[index]:
            result_bits[index] = first[index]
        else:
            break
        index += 1
    return toDecimal(result_bits)
    
    print(first)
    print(second)
    print(result_bits)

if __name__ == "__main__":
    print(rangeBitwiseAnd(1, 2147483647))