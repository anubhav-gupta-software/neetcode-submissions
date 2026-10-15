class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        new_nums = []
        for i, num in enumerate(nums):
            new_nums.append((num, i))
        
        new_nums = sorted(new_nums)

        i, j = 0, len(new_nums) - 1
        while i < j:
            if target > new_nums[i][0] + new_nums[j][0]:
                i += 1
            elif target < new_nums[i][0] + new_nums[j][0]:
                j -= 1
            else:
                return [new_nums[i][1], new_nums[j][1]]

