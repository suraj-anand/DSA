def removeElement(nums, val):
    i = 0
    j = len(nums) - 1
    k = 0
    
    while i <= j:
        if nums[i] == val and nums[j] != val:
            k += 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        elif nums[j] == val:
            k += 1
            j -= 1
        elif nums[i] != val:
            i += 1
        else:
            k += 1
            i += 1
            j -= 1

    return k

nums = [0,1,2,2,3,0,4,2]
# nums = [3, 2, 2, 3]
val = 2
print(removeElement(nums=nums, val=val))

print(nums)