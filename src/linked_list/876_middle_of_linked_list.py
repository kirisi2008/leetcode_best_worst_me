# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        elif not head.next:
            return head
        
        fast, slow = head, head

        while fast != None:
            fast = fast.next.next
            slow = slow.next

            if fast == None or fast.next == None:
                return slow
        

# fast implementation
# Using one node and one counter rather than two nodes
def middleNode(self, head):
	#calculate the length of the linked list
    count = 0
    curr = head
    while curr:
        curr = curr.next 
        count += 1
	#traverse head to the middle
    for _ in range((count//2)):
        head = head.next 
    return head 