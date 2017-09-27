# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :Algo Complexity O(n)
        The distance of fast is X+mY+K, dis of slow is X+nY+k. The velocity of them are 2 and 1.
        So we can deduce that X+K = (m-2n)Y. From this we can know that, if slow start from head again and fast goes from the K point. 
        They will meet again at a point P. That point P is the place where cycles starts. 
        """
        if not head:
            return None
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        
