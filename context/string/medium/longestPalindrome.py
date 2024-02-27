def longestPalindrome(s):
    lastIndex = len(s) - 1
    left, right = 0, lastIndex
    longest_palindrome = ""
    
    while left != lastIndex + 1:
        if left-1 == right:
            left += 1
            right = lastIndex
        
        i, j = left, right
        isPalindrome = True
        while i < j:
            if s[i] != s[j]:
                isPalindrome = False
                break
            i += 1
            j -= 1
        if isPalindrome:
            palindrome = s[left: right + 1]
            return palindrome
        right -= 1
    return ""
if __name__ == "__main__":
    string = "cbbd"
    
    longestPalindrome = longestPalindrome(string)
    print(longestPalindrome)