class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lis = [1] * n
        global_lis = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[j] + 1, lis[i])
            global_lis = max(lis[i], global_lis)

        return global_lis
    