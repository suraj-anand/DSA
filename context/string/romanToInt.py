def romanToInteger(s):
    hashmap = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    
    value = 0
    prev = -1
    
    for i in list(s)[::-1]:
        current_int = hashmap.get(i)
        if prev > current_int:
            value -= current_int
        else:
            value += current_int 
        prev = int(hashmap.get(i))
    
    return value

if __name__ == "__main__":
    roman = "MCMXCIV"
    print(romanToInteger(roman))