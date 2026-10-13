class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        max_reach = nums[0]
        for i in range(1, n-1):
            if max_reach < i:
                return False
            max_reach = max(nums[i] + i, max_reach)
        
        
        return True 