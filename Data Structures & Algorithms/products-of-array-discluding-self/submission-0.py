class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
                continue
            product *= num
        
        final = []
        if count_zero > 1:
            return [0] * len(nums)
        elif count_zero == 1:
            for num in nums:
                if num == 0:
                    final.append(product)
                else: 
                    final.append(0)
        else:
            for num in nums:
                final.append(int(product/num))
        
        return final