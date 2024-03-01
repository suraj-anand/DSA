def isSubsequence(s: str, t: str) -> bool:
    m = len(s)
    n = len(t)
    
    left, right = 0, 0
    
    while left < m and right < n:
        if s[left] == t[right]:
            left += 1
            right += 1
        else:
            right += 1
    
    return left == m and right == n

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))