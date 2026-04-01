# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = head
        before = ListNode()
        before_dummy = before
        after = ListNode()
        after_dummy = after
        counter = 1
        while dummy:
            if counter < left:
                before_dummy.next = ListNode(dummy.val)
                before_dummy = before_dummy.next
            elif counter > right:
                after_dummy.next = ListNode(dummy.val)
                after_dummy = after_dummy.next
            
            dummy = dummy.next
            counter += 1

        before = before.next
        after = after.next
        prev = head
        curr = None
        counter = 1
        while prev:
            next_node = prev.next
            if left <= counter <= right:
                prev.next = curr
                curr = prev

            prev = next_node
            counter += 1

        if before:
            result = before
            while before.next:
                before = before.next
            before.next = curr
            
            while before.next:
                before = before.next
            before.next = after
        else:
            result = curr
            
            while curr.next:
                curr = curr.next
            curr.next = after

        
        return result
