# Approach 1
def findMissing(nums):
    n = len(nums)
    expected_sum = (n * (n+1)) // 2

    actual_sum = 0
    for (index, element) in enumerate(nums):
        actual_sum += element

    return ( expected_sum - actual_sum ) 

# Approach 2 - XOR
def findMissing(nums):
    n = len(nums)
    XOR1 = 0 # Expected
    XOR2 = 0 # Actual
    for (index, element) in enumerate(nums):
        XOR1 ^= index
        XOR2 ^= element
    XOR1 ^= n

    return XOR2 ^ XOR1


nums = [9,6,4,2,3,5,7,0,1]
print(findMissing(nums=nums))