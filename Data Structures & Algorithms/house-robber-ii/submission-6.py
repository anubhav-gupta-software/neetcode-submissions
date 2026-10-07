class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        mm1 = [0] * n
        mmn = [0] * n
        mm1[1] = nums[1]
        mmn[0], mmn[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            mm1[i] = max(nums[i] + mm1[i-2], mm1[i-1])
            mmn[i] = max(nums[i] + mmn[i - 2], mmn[i - 1])
        return max(mm1[n-1] , mmn[n-2])
        