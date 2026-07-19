class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_cost = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_cost = max(max_cost, prices[j] - prices[i])
        return max_cost