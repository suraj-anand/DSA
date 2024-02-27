def commonChars( words: list) -> list:
    
    hashmap = {}
    nWords = len(words)
    
    for word in words:
        for char in word:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
    print(hashmap)
    
    result = []
    for key, value in hashmap.items():
        occurence = (value // nWords)
        if occurence > 0:
            for i in range(occurence):
                result.append(key)
    return result

if __name__ == "__main__":
    words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
    # words = ["cool","lock","cook"]
    print(commonChars(words))