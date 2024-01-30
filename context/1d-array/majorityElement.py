def majorityElement(nums):
    hashmap = {}
    majority = (len(nums) // 2 ) + 1 
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
            if hashmap[num] == majority:
                return num
        else:
            hashmap[num] += 1
            nth = hashmap[num]
            if nth == majority:
                return num

if __name__ == "__main__":
    nums = [1]
    # nums = [3,2,3]
    print(majorityElement(nums))