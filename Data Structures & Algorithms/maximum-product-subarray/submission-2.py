class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_ending = nums[0]
        max_ending = nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            tmp = min_ending
            min_ending = min(nums[i], max_ending * nums[i], min_ending * nums[i])
            max_ending = max(nums[i], max_ending * nums[i], tmp * nums[i])

            max_prod = max(max_prod, max_ending)
        
        return max_prod