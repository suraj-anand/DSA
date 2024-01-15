def splitSquareAndSum(n):
    answer = 0
    while n != 0:
        lastDigit = n % 10
        answer = answer + (lastDigit * lastDigit)
        n = n // 10
    return answer

class Solution:
    def isHappy(self, n: int) -> bool:
        result = splitSquareAndSum(n)
        while result >= 10:
            result = splitSquareAndSum(result)
        
        return result == 1

s = Solution()
print(s.isHappy(1111111))