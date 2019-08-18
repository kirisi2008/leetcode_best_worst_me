# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        answer = 0
        length = len(height)
        left_max, right_max = [0] * length, [0] * length
        
        left_max[0], right_max[-1] = height[0], height[-1]
        # Actually one can loop twice here with left cursor and Right cursor.
        for left_pr in range(1, length):
            left_max[left_pr] = max(height[left_pr], left_max[left_pr-1])
            right_max[length - left_pr - 1] = max(height[length - left_pr - 1], right_max[length - left_pr])
            # print(left_pr, left_max[left_pr], length - left_pr - 1, right_max[length - left_pr - 1])
        
        for pr in range(1, length - 1):
            answer += min(right_max[pr], left_max[pr]) - height[pr]
            
            
        return answer