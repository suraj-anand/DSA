def closeStrings(str1, str2) -> bool:
    hashmap1, hashmap2 = {}, {}
    for i in str1:
        hashmap1[i] = hashmap1.get(i, 0) + 1
    
    for i in str2:
        hashmap2[i] = hashmap2.get(i, 0) + 1
    
    
    return True

if __name__ == "__main__":
    s1 = ""
    s2 = ""
    r = closeStrings(s1, s2)
    print(r)