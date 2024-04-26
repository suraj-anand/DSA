def removeDuplicates(nums):
    hashset = set()
    n = len(nums)
    
    left = 0
    X = 0
    while left < n:
        if nums[left] not in hashset:
            hashset.add(nums[left])
            left += 1
        else:
            right = X + 1
            while right < n:
                if nums[right] not in hashset:
                    hashset.add(nums[right])
                    nums[left], nums[right] = nums[right], nums[left]
                    X = right
                    break
                right += 1
            left += 1
    return len(hashset)


if __name__ == "__main__":
    nums = [1,0,0,1,1,2,1,3,1,4]
    l = removeDuplicates(nums)
    print(nums)
    print(l)