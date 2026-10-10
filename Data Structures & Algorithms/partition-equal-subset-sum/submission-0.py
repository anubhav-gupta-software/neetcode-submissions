class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 == 1:
            return False
        target = sum // 2
        
        canMake = [False] * (target + 1)
        canMake[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                canMake[i] = canMake[i] or canMake[i - num]
        
        return canMake[target]