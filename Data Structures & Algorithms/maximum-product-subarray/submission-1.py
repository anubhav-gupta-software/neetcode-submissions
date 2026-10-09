class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_ending = nums[:]
        max_ending = nums[:]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            min_ending[i] = min(nums[i], max_ending[i - 1] * nums[i], min_ending[i - 1] * nums[i])
            max_ending[i] = max(nums[i], max_ending[i - 1] * nums[i], min_ending[i - 1] * nums[i])
        
            max_prod = max(max_prod, max_ending[i])
        
        return max_prod