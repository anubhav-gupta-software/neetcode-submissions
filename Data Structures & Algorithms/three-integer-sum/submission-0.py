class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums  = sorted(nums)
        for index in range(len(nums) - 1):
            i = index + 1
            j = len(nums) - 1
            if index > 0 and nums[index] == nums[index-1]:
                continue
            if nums[index] > 0:
                break
            while i < j:
                target = nums[index] + nums[i] + nums[j]
                if target == 0:
                    answer.append([nums[index], nums[i], nums[j]])
                    i+= 1
                    while i < j and nums[i] == nums[i-1]:
                        i+= 1
                    j-= 1
                    while i < j and nums[j] == nums[j+1]:
                        j-= 1
                elif target > 0:
                    j-=1
                else:
                    i+=1

        return answer