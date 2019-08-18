# We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

# Example 1:
# Input: 
# bits = [1, 0, 0]
# Output: True
# Explanation: 
# The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
# Example 2:
# Input: 
# bits = [1, 1, 1, 0]
# Output: False
# Explanation: 
# The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
# Note:

# 1 <= len(bits) <= 1000.
# bits[i] is always 0 or 1.

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        count = 0
        while count < len(bits):
            if bits[count] == 0:
                count += 1
            else:
                count += 2
                if count == len(bits):
                    return False
        
        return True

# More mathematically correct solution
class Solution2(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1 or bits[-2] == 0:
            return True
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                continue
            if len(bits) % 2 == 0:
                if i == len(bits) - 1:
                    return True
                elif i == len(bits) - 2 and bits[i] == 0:
                    return True
                elif i == len(bits) - 2 and bits[i] == 1:
                    return False
            elif len(bits) % 2 == 1:
                if i == len(bits) - 1:
                    return True
            i += 1
        return False