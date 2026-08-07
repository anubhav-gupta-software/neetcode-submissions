class Solution:
    def trap(self, height: List[int]) -> int:
        height_max = 0
        max_left = height.copy()
        max_right = height.copy()
        for i in range(len(max_left)):
            max_left[i] = height_max = max(height_max, max_left[i])
        height_max = 0
        for i in range(len(max_right) - 1, -1, -1):
            max_right[i] = height_max = max(height_max, max_right[i])
        
        total = 0
        for i in range(len(height)):
            total += min(max_left[i], max_right[i]) - height[i]

        return total