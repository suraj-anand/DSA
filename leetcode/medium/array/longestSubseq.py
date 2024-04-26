def longestConsecutive(arr: list) -> int:
    n = len(arr)
    s = set(arr)
    longest = 0
    for i in arr:
        count = 1
        if (i-1) in s:
            continue
        
        for x in range(i+1, i+n+1):
            if x in s:
                count += 1
            else:
                break        
        longest = max(longest, count)
    return longest
    
    
if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(longestConsecutive(nums))

