# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

# For example, with A = "abcd" and B = "cdabcdab".

# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

# Note:
# The length of A and B will be between 1 and 10000.

import math

# Runtime Error
class Solution1(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        for A_pr in range(len(A)):
            if A[A_pr] == B[0]:
                count = 1
                B_pr = 0
                startIndex = A_pr
                while B_pr < len(B) and A[startIndex] == B[B_pr]:
                    B_pr += 1
                    startIndex += 1
                    if startIndex >= len(A) and B_pr < len(B):
                        startIndex = startIndex % len(A)
                        count += 1
                    
                if len(B) == B_pr:
                    return count
                
        return -1
        
# Good Solution
class Solution2(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        

        
        # some leetcode bug the a / b == math.ceil(a/b)
        count = (len(B) - 1) // len(A) + 1
        # count = int(math.ceil(len(B) / len(A)))
#         print(len(B), len(A), len(B) / len(A))
#         print(math.ceil(len(B) / len(A)))
#         print((len(B) - 1) // len(A) + 1)
        
        if B in A * count:
            return count
        if B in A * (count + 1):
            return count + 1
        return -1

# Fast Solution
class Solution3(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        if not set(B).issubset(set(A)):
            return -1

        base = len(B) / len(A)
        if len(B) % len(A) !=0:
            base += 1
        for i in range(2):
            if B in A * (base + i):
                return base + i
        return -1