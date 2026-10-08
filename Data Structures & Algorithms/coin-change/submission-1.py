class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        least = [float('inf')] * (amount + 1)
        least[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                least[i] = min(least[i], least[i - coin] + 1) 
        
        return least[amount] if least[amount] != float('inf') else -1