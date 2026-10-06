class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev, curr = cost[0], cost[1]
        for i in range(2, n):
            tmp = curr
            curr = cost[i] + min(prev, curr)
            prev = tmp
        return min(prev, curr)