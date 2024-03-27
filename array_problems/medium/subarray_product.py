def numSubarrayProductLessThanK(nums: list[int], k: int):
    left, right = 0, 0
    length = len(nums)
    count = 0
    prod = None
    
    while right < length:
        if not prod:
            prod = nums[right]
        else:
            prod *=nums[right]
        if prod < k:
            count += (right - left + 1)
        else:
            while prod >= k and left < right and right < length:
                prod //= nums[left]
                left += 1
                if prod < k:
                    count += (right - left + 1)
        right += 1
        
    
    return count
    
    
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    k = 1
    r = numSubarrayProductLessThanK(nums, k)
    print(r)