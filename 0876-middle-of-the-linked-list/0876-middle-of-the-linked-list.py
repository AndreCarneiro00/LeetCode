# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr = head
        size = 0

        while ptr.next:
            ptr = ptr.next
            size += 1
        
        res = head
        if size % 2 == 0:
            iterator = range(size / 2)
        else:
            iterator = range(size / 2 + 1)

        for i in iterator:
            res = res.next
        
        return res