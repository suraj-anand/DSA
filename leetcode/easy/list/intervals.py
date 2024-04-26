from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    start, last = 0, 0
    r = []
    for i in range(1, len(nums)):
        diff = nums[i-1] - nums[i]
        if diff != 1:
            if i == 1:
                r.append(f"{nums[]}")

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    r = summaryRanges(nums)
    print(r)