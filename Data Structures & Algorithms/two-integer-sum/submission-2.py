class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]