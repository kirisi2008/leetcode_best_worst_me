import json


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        elif not head.next:
            return head
        
        connect = [head]
        temp = head.next
        while temp:
            connect.append(temp)
            temp = temp.next
            
        left_p, right_p = 0, len(connect) -1
        
        while left_p < right_p:
            left = connect[left_p]
            right = connect[right_p]
            tmp_left_next = left.next
            left.next = right
            if right == tmp_left_next:
                right.next = None
            else:
                right.next = tmp_left_next
                
            left_p +=1
            right_p -=1
                
            if left_p == right_p:
                tmp_left_next.next = None
        return head


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


node = stringToListNode("[1, 2, 3, 4]")
print(listNodeToString(Solution().reorderList(node)))
