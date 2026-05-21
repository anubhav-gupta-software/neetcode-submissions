class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set()
        for i in nums:
            a.add(i)
        glo_count = 0
        for i in a:
            count = 1
            j = i
            while j-1 in a:
                count += 1
                j-= 1 
            if glo_count < count:
                glo_count = count
        return glo_count