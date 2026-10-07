class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def robline(arr):
            prev, curr = 0, 0

            for num in arr:
                prev, curr = curr, max(prev + num, curr)
            return curr
        return max(robline(nums[1:]), robline(nums[:-1]))

            
