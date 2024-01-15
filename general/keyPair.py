def hasArrayTwoCandidates(arr, n, x):
    hmap = {}

    for i, n in enumerate(arr):
        if n >= x:
            continue

        if hmap.get(n) not in hmap:
            hmap[n] = abs(x - n)
        else:
            return True
    return False

arr = [1, 4, 45, 6, 10, 8]
N = 6
X = 16
print(hasArrayTwoCandidates(arr, N, X))