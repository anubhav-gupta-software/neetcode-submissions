class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for money in nums:
            tmp = curr
            curr = max(money + prev, curr)
            prev = tmp

        return curr