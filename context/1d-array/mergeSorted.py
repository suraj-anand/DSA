def merge(nums1, m, nums, n):
    A = m - 1
    B = n - 1
    C = len(nums1) - 1
    print(A, B, C)
    
    while A > -1 and B > -1 and C > -1:
        if nums1[C] <= nums[B] and nums1[A] <= nums[B]:
            nums1[C] = nums[B]
            C -= 1
            B -= 1
        
        elif nums1[C] < nums[B] and nums1[A] > nums[B]:
            nums1[C] = nums1[A]
            A -= 1
            C -= 1
        
        else:
            A -= 1
            B -= 1
            C -= 1
    
    while B > -1 and C > -1:
        nums1[C] = nums[B]
        C -= 1
        B -= 1
        
    
arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
m = 3
n = len(arr2)
merge(arr1, m, arr2, n)
print("merged: ", arr1)