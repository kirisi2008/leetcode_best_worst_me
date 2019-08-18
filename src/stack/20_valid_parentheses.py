# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        keyDict = {')':'(', ']':'[', '}':'{'}
        pramList = []
        length = len(s)
        pr = 0
        
        if not s:
            return True
        elif s[0] in [')', ']', '}']:
            return False
        
        while pr < length:
            paren = s[pr]
            if paren in ['(', '[', '{']:
                pramList.append(paren)
            elif not pramList:
                return False
            elif pramList[-1] == keyDict[paren]:
                pramList.pop()
            else:
                return False
            pr += 1
            
        return True if not pramList else False
                
        