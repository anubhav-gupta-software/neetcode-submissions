class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            tmp = curr
            curr = max(curr, nums[i] + prev)
            prev = tmp
            
        return curr
