# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Example 1:

# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:

# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:

# Input: ")("
# Output: [""]

class Solution(object):
    
    def find_delete(self, s):
        x = 0
        left_p, right_p = 0, 0
        l_need_delete, r_need_delete = 0, 0
        for c in s:
            if c == '(':
                x += 1
                left_p += 1
            elif c == ')':
                right_p += 1
                if x > 0:
                    x -= 1
                else:
                    r_need_delete += 1
        l_need_delete = x
        return (left_p, right_p, l_need_delete, r_need_delete)
        
    def removeInvalidParentheses(self, s):
        def dfs(x, curr_s, i, n, l_p, r_p, l_del, r_del):
            if i == n:
                if l_del == 0 and r_del == 0:
                    res.add(curr_s)
                return
            if s[i] == '(':
                if l_p == l_del: # must delete it
                    dfs(x, curr_s, i + 1, n, l_p - 1, r_p, l_del - 1, r_del)
                else:
                    # allowed to keep it
                    dfs(x + 1, curr_s + '(', i + 1, n, l_p - 1, r_p, l_del, r_del)
                    if l_del > 0: # allowed to delete it
                         dfs(x, curr_s, i + 1, n, l_p - 1, r_p, l_del - 1, r_del)
            elif s[i] == ')':
                if r_p == r_del: # must delete it
                    dfs(x, curr_s, i + 1, n, l_p, r_p - 1, l_del, r_del - 1)
                else:
                    if x > 0: # allowed to keep it
                        dfs(x - 1, curr_s + ')', i + 1, n, l_p, r_p - 1, l_del, r_del)
                    if r_del > 0: # allowed to delete it
                        dfs(x, curr_s, i + 1, n, l_p, r_p - 1, l_del, r_del - 1)
            else:
                dfs(x, curr_s + s[i], i + 1, n, l_p, r_p, l_del, r_del)
        
        l_p, r_p, l_del, r_del = self.find_delete(s)
        res = set()
        dfs(0, '', 0, len(s), l_p, r_p, l_del, r_del)
        return list(res)