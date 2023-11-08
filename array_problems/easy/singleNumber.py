# Without Extra Space
def singleNumber(nums):
    n = len(nums)
    
    XOR1 = 0 
    for (index, element) in enumerate(nums):
        XOR1 ^= element
    
    return XOR1

nums = [2,2,1]
print(singleNumber(nums))

nums = [4,1,2,1,2]
print(singleNumber(nums))

nums = [1]
print(singleNumber(nums))