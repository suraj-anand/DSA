def frequencySort(s):
    hashmap = {}
    
    for char in s:
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] += 1
    
    output = ""
    for key in sorted(hashmap, key=hashmap.get, reverse=True):
        output += key * hashmap[key]
    
    return output
    
if __name__ == "__main__":
    string = "Aabb"
    print(frequencySort(string))