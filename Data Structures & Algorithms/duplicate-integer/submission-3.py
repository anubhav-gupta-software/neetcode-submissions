class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums:
            a[i] = a.get(i, 0) + 1
            if a[i] > 1:
                return True
        return False              
        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        
        # return False