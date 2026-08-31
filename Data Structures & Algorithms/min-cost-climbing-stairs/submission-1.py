class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost)+1)
        prev, curr = 0, 0
        for i in range(2, len(cost) + 1):
            tmp = curr
            curr = min(cost[i - 1] + curr, cost[i - 2] + prev)
            prev = tmp
        
        return curr
