def isVowel(c: str):
    return c.lower() in ["a", "e", "i", "o", "u"]

def swap(string_array, i, j):
    string_array[i], string_array[j] = string_array[j], string_array[i]
    
def reverseVowels(string: str):
    
    string_array = list(string)
    i , j = 0, len(string_array) - 1
    
    
    while i < j:
        if isVowel(string_array[i]) and isVowel(string_array[j]):
            swap(string_array, i, j)
            i += 1
            j -= 1
            
        if not isVowel(string_array[i]):
            i += 1
        
        if not isVowel(string_array[j]):
            j -= 1
        
    return "".join(string_array)

print(reverseVowels("leetcode"))