def similarEnds(s: str) -> str:
    length = len(s)
    if length <= 1:
        return length
    
    left, right = 0, length - 1
    
    while left < right:

        if s[left] != s[right]:
            break
        
        while left < length:
            if left + 1 >= length:
                break
            if s[left] == s[left + 1]:
                left += 1
            else:
                break

        while right > 0:
            if right - 1 < 0:
                break
            if s[right] == s[right - 1]:
                right -= 1
            else:
                break
        
        print(left, right)
        left += 1
        right -= 1

    print(right, left)
    if  right< left:
        return 0
    return ((right - left) + 1)

if __name__ == "__main__":

    # string = "aabccabba"
    string = "bbbbbbbbbbbbbbbbbbb"
    s = similarEnds(string)
    print(s)