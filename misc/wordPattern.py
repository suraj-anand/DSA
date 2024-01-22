def wordPattern(pattern, s):
    i, n = 0, len(pattern)
    words = s.split(" ")
    hashmap = {}
    
    if len(words) != n:
        return False
    
    while i < n:
        if pattern[i] not in hashmap.keys():
            if words[i] in hashmap.values():
                return False
            hashmap[pattern[i]] = words[i]
            i += 1
        else:
            if hashmap[pattern[i]] == words[i]:
                i += 1
            else:
                return False
    return True

print(wordPattern(pattern="aaaa",s="dog dog dog dog"))