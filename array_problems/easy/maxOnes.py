def findMaxConsecutiveOnes(nums):
    max_ones, count = 0, 0

    for (index, element) in enumerate(nums):
        if element == 1:
            count += 1
        else:
            if count > max_ones:
                max_ones = count
            count = 0
    if count > max_ones:
        max_ones = count
    return max_ones

nums = [1,1,1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))