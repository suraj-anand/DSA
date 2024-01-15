# Approach #1: Brute
def rotate_array(array: list, k):
    k = k % len(array)

    for _ in range(k):
        temp = -1
        for i in range(len(array)-1, -1, -1):
            if i == (len(array) - 1):
                temp = array[i]
                print(temp)
                continue
            array[i+1] = array[i]
        array[0] = temp
    return array


def reverse(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1 

# Approach 2: O(n/2 + (k) + (n-k))
def rotate_array_2(array: list, k):
    k = k % len(array)
    n = len(array)

    left, right = 0, n -1
    reverse(array, left, right)

    left, right = 0, k - 1
    reverse(array, left, right)
    
    left, right = k, n - 1
    reverse(array, left, right)
    
    return array

print(rotate_array_2([1, 2, 3, 4], 2))