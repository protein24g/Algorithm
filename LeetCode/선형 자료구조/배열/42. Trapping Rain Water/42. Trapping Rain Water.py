class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        value = 0
        
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] <= height[right]:
                value += left_max - height[left]
                left += 1
            else:
                value += right_max - height[right]
                right -= 1
                
        return value
