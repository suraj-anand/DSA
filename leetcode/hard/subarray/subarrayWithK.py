# 992. Subarrays with K Different Integers
def subarraysWithKDistinct(nums: list[int], k: int) -> int:
    n = len(nums)
    subarrays = []
    
    for i in range(n):
        for j in range(i+k, n):
            print(nums[i:j+1])
            subarray = set(nums[i:j+1])
            if len(subarray) == k:
                subarrays.append(subarray)
    
    return len(subarrays)

if __name__ == "__main__":
    nums = [1,2,1,2,3]
    # nums = [1, 2]
    k = 2
    result = subarraysWithKDistinct(nums, k)
    print(result)