class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set()
        for num in nums:
            if num in set_num:
                return False
            set_num.add(num)
        return True