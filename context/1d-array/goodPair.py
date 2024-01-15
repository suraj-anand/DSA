# Approach #1 - O(n^2)
def good_pair(array, n):
    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == n:
                return 1
    return 0

# Apporach # 2 - O(n)
def good_pair_2(array, n):
    hashset = set()
    for i in range(len(array)):
        if array[i] in hashset:
            return 1
        else:
            hashset.add(abs(n-array[i]))
    return 0

arrays = (
    [1,2,3,4], [1,2,4], [1,2,2]
)

n = (
    7, 4, 4
)


for array, n in zip(arrays, n):
    print(good_pair_2(array=array, n=n))