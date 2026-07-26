class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currPrice = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            currProfit = prices[i]-currPrice
            profit = max(profit,currProfit)
            currPrice = min(currPrice,prices[i])
        return profit
        