## Leetcode: 70

def nStairs(n):
    if n <= 1:
        return 1
    else:
        return nStairs(n - 1) + nStairs(n - 2)
    
def nStairsIterative(n):
    a, b = 0, 1
    c = -1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return c
    
for n in range(1, 11):
    print(nStairsIterative(n))
