class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = nums.copy()
        max_rob[0] = nums[0]
        for i in range(1, len(nums)):
            max_rob[i] += max_rob[i - 2] if i >= 2 else 0
         
        return max(max_rob[len(nums) - 1], max_rob[len(nums) - 2] if len(nums) >= 2 else 0)
