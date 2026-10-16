class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = -prices[0] #holding a stock
        sold = 0 #sold the stock today
        rest = 0 #not holding anything and didnt sell today

        for i in range(1, len(prices)):
            new_hold = max(hold, rest - prices[i])
            new_sold = hold + prices[i]
            new_rest = max(sold, rest)

            hold, sold, rest = new_hold, new_sold, new_rest
        
        return max(sold, rest)