class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #when using sorted, creates a new list
        #nums.sort() for close to O(1) space.
        #set.add 
 
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False