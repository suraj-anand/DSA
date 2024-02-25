def gcdOfStrings(str1: str, str2: str) -> str:
    hashmap = {}
    for char in str1:
        hashmap[char] = hashmap.get(char, 0) + 1
    
    r = ""
    for char in str2:
        r += char
        copy = hashmap.copy()
        for c in r:
            if c in copy:
                del copy[c]
            else:
                copy[c] = 1
        print(r, copy)
        if len(copy) == 0:
            return r
    return r

if __name__ == "__main__":
    str1 = "LEET"
    str2 = "CODE"
    print(gcdOfStrings(str1, str2))
