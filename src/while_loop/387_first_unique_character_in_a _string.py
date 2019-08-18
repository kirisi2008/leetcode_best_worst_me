# Given a string, find the first non-repeating character in it and return
# it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        elif len(s) == 1:
            return 0

        resultSet = {}
        stringList = []
        for index, char in enumerate(s):
            if char in resultSet:
                resultSet[char] = -1
            else:
                stringList.append(char)
                resultSet[char] = index

        for char2 in stringList:
            if resultSet[char2] >= 0:
                return resultSet[char2]

        return -1


# sampleTestCase = [
#     "leetcode"
#     "aaaaaa"
#     "aaaab"
#     "ac"
#     ""
# ]
