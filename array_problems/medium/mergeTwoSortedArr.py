class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Merge Procedure from merge-sort
        left, right = 0, 0
        m, n = len(nums1), len(nums2)
        result = []

        while left < m and right < n and nums1[left] != 0:
            if nums1[left] < nums2[right]:
                result.append(nums1[left])
                left += 1
            
            else:
                result.append(nums2[right])
                right += 1

        while left < m:
            if nums1[left] != 0:
                result.append(nums1[left])
            left += 1

        while right < n:
            result.append(nums2[right])
            right += 1

        for (index, element) in enumerate(result):
            nums1[index] = element

s = Solution()

nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]
s.merge(nums1, m=len(nums1), nums2=nums2, n=len(nums2))