# lc-1768
def mergeAlternately(word1: str, word2: str):
    i = j = 0
    m, n = len(word1), len(word2)
    index = 0
    result = ""
    
    while i < m or j < n:
        if index % 2 == 0 and i < m:
            result += word1[i]
            i += 1
        elif index % 2 != 0 and j < n:
            result += word2[j]
            j += 1
        elif i < m:
            result += word1[i]
            i += 1
        elif j < n:
            result += word2[j]
            j += 1
        index += 1
    return result

print(mergeAlternately("abcd", "pq"))