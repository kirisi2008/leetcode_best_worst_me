# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height[0], height[1])
        
        # Using double pointer
        left_p, right_p = 0, len(height) - 1
        max_volumn = 0
        
        while left_p < right_p:
            max_volumn = max(max_volumn, min(height[left_p], height[right_p]) * (right_p - left_p))
            if height[left_p] <= height[right_p]:
                left_p += 1
            else:
                right_p -= 1
        
        return max_volumn