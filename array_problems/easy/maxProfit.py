def maxProfitBrute(prices):
    max_profit = 0
    n = len(prices)

    for i in range(n):
        purchased = prices[i]
        for j in range(i+1, n):
            current_rate =  prices[j] - purchased
            if current_rate > max_profit:
                max_profit = current_rate
    return max_profit

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) > 0:
            purchased = prices[0]
        max_profit = 0

        # Optimal
        for price in prices:
            if price < purchased:
                purchased = price
            result = price - purchased
            if  result > max_profit:
                max_profit =  result
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(
s.maxProfit(prices)
)