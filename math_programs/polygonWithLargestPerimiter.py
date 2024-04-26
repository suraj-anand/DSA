
def polygonWithLargestPerimiter(nums):
    n = len(nums)
    # base case
    if n < 3:
        return -1
    
    nums = sorted(nums)
    result = -1
    total = 0
    for i in nums:
        if i < total:
            result = i
        total += i
    return result
        
if __name__ == "__main__":
    nums = [1,12,1,2,5,50,3]
    # nums = [5, 5, 5]
    # nums = [1, 1, 2]
    
    # nums = [5, 5, 50]
    r = polygonWithLargestPerimiter(nums)
    print(r)