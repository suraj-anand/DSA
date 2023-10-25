# Two Pointer approach
# def reverse(arr, i, j):
#     if i >= j:
#         return
#     arr[i], arr[j] = arr[j], arr[i]
#     reverse(arr, i=i + 1, j=j - 1)


# One Pointer
def reverse(arr, i):
    if i >= n // 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverse(arr, i=i + 1)


arr = [10, 20, 30, 40, 50]
n = len(arr)
# reverse(arr, i=0, j=len(arr) - 1) # Two Pointer Approach func call
reverse(arr, i=0)  # Two Pointer Approach func call
print(arr)
