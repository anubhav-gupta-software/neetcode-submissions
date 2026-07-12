class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        for i in nums:
            if i == 0:
                count_zero += 1
                continue
            product *= i
        if count_zero > 1:
            return [0] * len(nums)
        final = [] 
        for i in nums:
            if count_zero:
                if i == 0: 
                    final.append(product)
                else:
                    final.append(0)
            else:
                final.append((product//i))
        return final