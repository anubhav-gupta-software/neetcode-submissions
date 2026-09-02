class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robline(arr):
            prev, curr = 0, 0
            for money in arr:
                tmp = curr
                curr = max(money + prev, curr)
                prev = tmp
            return curr

        return max(robline(nums[:-1]), robline(nums[1:]))