def floorRoot(n):
    low, high = 1, n
    
    while low <= high:
        mid = (low + high) // 2
        if mid <= n // mid:
            sqrt = mid
            low = mid + 1
        else:
            high = mid - 1
    return sqrt

def checkPerfectNumber(num):
    sum = 0
    print(f"floorRoot: {floorRoot(num)}")
    print("factors: 1, ", end="")
    for i in range(2, floorRoot(num) + 1):
        if num % i == 0:
            print(i, num//i,end=" ")
            sum += i
            sum += (num//i)
    print(f"Sum => {sum}")
    return num == (sum + 1)

n = int(input("Enter the number: "))
print(checkPerfectNumber(n))