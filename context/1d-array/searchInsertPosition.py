def searchInsert(nums, target):
    low, high = 0, len(nums)
    
    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            high = mid - 1
            
        else:
            low = mid + 1
    
    print(low, mid, high)
    # if mid == 0:
    #     return mid
    return mid + 1

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 0
    
    print(searchInsert(nums, target))
