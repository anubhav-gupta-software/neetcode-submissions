class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        l, r = 0, len(height) - 1
        total = 0

        while l < r:
            if height[l] <= height[r]:
                max_left = max(max_left, height[l])
                total += max_left - height[l]
                l+= 1
            else:
                max_right = max(max_right, height[r])
                total += max_right - height[r]
                r -= 1
        return total