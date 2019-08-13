# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or (not l1.next and l1.val == 0):
            return l2
        elif l2 == None or (not l2.next and l2.val == 0):
            return l1
        
        temp1, temp2 = l1, l2
        num1, num2 = 0, 0
        multi1, multi2 = 1,1
        head = ListNode(None)
        reply = head
        # turn them into int
        while temp1 or temp2:
            if temp1:
                num1 = num1 + multi1 * temp1.val 
                multi1 *= 10
                temp1 = temp1.next
            if temp2:
                num2 = num2 + multi2 * temp2.val
                multi2 *= 10
                temp2 = temp2.next
        # add two int
        result = num1 + num2
        # generate new linked list
        while result > 0:
            val = result % 10
            head.next = ListNode(val)
            head = head.next
            result = result // 10
        
        return reply.next