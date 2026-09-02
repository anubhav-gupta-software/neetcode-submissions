class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = [0] * len(nums)
        for i in range(len(nums)):
            max_money[i] = max(nums[i] + (max_money[i - 2] if i >= 2 else 0), max_money[i - 1] if i >= 1 else 0)

        return max_money[len(nums) - 1] 