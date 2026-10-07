class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        for i in range(1, n):
            i_2 = 0
            if i != 1:
                i_2 = max_money[i-2]
            max_money[i] = max(max_money[i - 1], nums[i] + i_2)
    
        return max_money[n-1]
        