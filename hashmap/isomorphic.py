def isIsomorphic(s: str, t: str) -> bool:
    m, n = len(s), len(t)
    if m != n:
        return False
    
    hashmap = {}
    for i in range(m):
        
        lchar = s[i]
        rchar = t[i]
        print(lchar, rchar, hashmap)
        
        if lchar not in hashmap:
            if rchar in hashmap.values():
                return False
            hashmap[lchar] = rchar
        if hashmap[lchar] != rchar:
            return False
    return True

if __name__ == "__main__":
    s = "paper"
    t = 'title'
    
    s = "badc"
    t = "babc"
    r = isIsomorphic(s, t)
    print(r)

# ""