class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        max_money = [0] * len(nums)
        max_money[0], max_money[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            max_money[i] = max(max_money[i - 1], nums[i] + max_money[i - 2])
    
        return max_money[n-1]
