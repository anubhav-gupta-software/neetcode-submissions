class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        least = [float('inf')] * (amount + 1)
        least[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    least[i] = min(least[i], least[i - coin] + 1) 
        
        return least[amount] if least[amount] != float('inf') else -1