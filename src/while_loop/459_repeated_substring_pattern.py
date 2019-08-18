# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

# Example 1:

# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:

# Input: "aba"
# Output: False
# Example 3:

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution1(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        
        length = 1
        
        while length < len(s):
            # break into substring lists.
            subset = [s[a*length:a*length+length] for a in range(len(s) // length)]
            if len(set(subset)) == 1:
                return True
            length += 1
            while len(s) % length != 0:
                length += 1
        return False


# Clever solution
class Solution2(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr = s[1:] + s[:-1]
        return newstr.find(s) != -1