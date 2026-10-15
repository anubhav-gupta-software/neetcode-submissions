class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        max_reach = 0
        curr_reach = 0
        
        for i in range(len(nums)):
            if i > curr_reach:
                curr_reach = max_reach
                jumps += 1
            max_reach = max(max_reach, i + nums[i])

        return jumps