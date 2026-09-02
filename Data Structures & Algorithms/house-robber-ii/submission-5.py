class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robline(left, right):
            prev, curr = 0, 0
            for i in range(left, right):
                tmp = curr
                curr = max(nums[i] + prev, curr)
                prev = tmp
            return curr

        return max(robline(1, len(nums)), robline(0, len(nums) - 1))