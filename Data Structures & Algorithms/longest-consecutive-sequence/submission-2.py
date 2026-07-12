class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        max_len = 0
        for num in checker:
            if num - 1 in checker:
                continue
            local_max = 1
            j = num + 1
            while j in checker:
                local_max += 1
                j += 1
            max_len = max(max_len, local_max)
        return max_len