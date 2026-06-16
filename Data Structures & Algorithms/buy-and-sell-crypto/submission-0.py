class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        low = prices[0]
        for i in range(len(prices)):
            maxprofit = max(maxprofit,prices[i]-low)
            low = min(low,prices[i])
        
        return maxprofit
        