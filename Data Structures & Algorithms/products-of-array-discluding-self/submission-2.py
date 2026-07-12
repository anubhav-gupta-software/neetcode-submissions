class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            final[i] = final[i-1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            nums[i] *= nums[i+1]
        print(final)
        print(nums)
        for i in range(len(nums)):
            if i == 0:
                nums[i] = nums[i+1]
                continue
            if i == len(nums) - 1:
                nums[i] = final[i-1]
                continue
            nums[i] = final[i-1] * nums[i+1]
        return nums