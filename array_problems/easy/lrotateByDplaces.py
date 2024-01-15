# # Approach 1
# def rotateByD(arr, D):
#     n = len(arr)
#     D = D % n

#     temp = arr[:D]
#     for i in range(D, n):
#         arr[i-D], arr[i] = arr[i], arr[i-D]
    
#     j = 0
#     for i in range(D+1, n):
#         arr[i] = temp[j]
#         j += 1
    
#     print(f"rotated arr: {arr}")


# Approach 2, split and rotate
def inplace_rotate(arr, start, end):
    # start - inclusive, end - exclusive
    left, right = start, end-1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotateByD(arr, D):
    n = len(arr)
    D = D % n
    if D % 2 == 0:
        D = D - 1
    inplace_rotate(arr, 0, D+1)
    inplace_rotate(arr, D+1, n)
    inplace_rotate(arr, 0, n)
    print(f"rotated arr: {arr}")

array = [-1,-100,3,99]
rotateByD(array, D=2)