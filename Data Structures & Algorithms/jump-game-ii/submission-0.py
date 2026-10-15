class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        minnum = [float('inf')] * n
        minnum[0] = 0
        for i in range(n):
            for j in range(i+1, min(n, i + nums[i]+1)):
                minnum[j] = min(minnum[i] + 1, minnum[j])
        
        return minnum[n-1]