def equilibriumPoint(arr):
    left, right = 0, len(arr) - 1
    left_sum = right_sum = 0

    while left < right:
        left_sum += arr[left] 
        right_sum += arr[right]

        if left_sum == right_sum:
            return left + 2

        left += 1
        right -= 1

    return left + 2
array = [1]
print(equilibriumPoint(array))