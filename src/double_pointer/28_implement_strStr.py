# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        elif not haystack:
            return -1
        subStrLength = len(needle)
        subStrFistChar = needle[0]
        if subStrFistChar not in haystack:
            return -1
        
        for i in range(len(haystack) - subStrLength + 1):
            if haystack[i] == subStrFistChar:
                if self.isSubStr(needle, haystack[i:]):
                    return i
        return -1
                
     
    def isSubStr(self, target, string):
        for i in range(len(target)):
            if target[i] != string[i]:
                return False
        return True

# fast Implementation
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack or needle == '':
            return 0
        if haystack == '' or len(needle) > len(haystack):
            return -1
        for i in range(0, len(haystack) - len(needle) + 1):
            sub = haystack[i : i + len(needle)]
            print(sub)
            if needle == sub:
                return i
        return -1