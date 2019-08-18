# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):      
        start, longest, lastPosition = 0, 0, {}
        
        for end, c in enumerate(s):
            
            if c in lastPosition:
                start = max(start, lastPosition[c] + 1)
            
            lastPosition[c] = end
            # print(start, end, c, lastPosition)
            longest = max(longest, end-start+1)
            
        return longest