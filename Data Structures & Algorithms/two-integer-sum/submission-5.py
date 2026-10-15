class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in a:
                return [a[needed], i]
            a[num] = i
        
        return None