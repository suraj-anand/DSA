def isIsomorphic(s, t):
    hashmap1 = {}
    hashmap2 = {}
    
    if len(s) != len(t):
        return False
    
    for i, j in zip(s, t):
        if i not in hashmap1:
            hashmap1[i] = 1
        else:
            hashmap1[i] += 1
        
        if j not in hashmap2:
            hashmap2[j] = 1
        else:
            hashmap2[j] += 1
    
    if len(hashmap1.keys()) != len(hashmap2.keys()):
        return False
    
    if sorted(list(hashmap1.values())) != sorted(list(hashmap2.values())):
        return False
    
    print(hashmap1)
    print(hashmap2)
    
    return True
    

if __name__ == "__main__":
    s = "bbbaaaba"
    t = "aaabbbba"
    
    print(isIsomorphic(s,t)) 