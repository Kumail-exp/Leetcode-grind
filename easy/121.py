class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        ms=10001
        for i in range(len(prices)):
            ms=min(ms,prices[i])
            profit=max(profit,prices[i]-ms)
        return profit