from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap = {}

    for num in nums1:
        hashmap[num] = hashmap.get(num, 0) + 1
    
    result = []
    for num in nums2:
        if num in hashmap and hashmap[num] > 0:
            result.append(num)
            hashmap[num] -= 1
    return result

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    r = intersect(nums1, nums2)
    print(r)
        