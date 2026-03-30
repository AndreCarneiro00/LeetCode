# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        ll = head
        while ll:
            len_list += 1
            ll = ll.next
        
        if len_list <= 1:
            return

        if len_list == n:
            head = head.next
            return head
            
        ll = head
        counter = 0
        while ll:
            counter += 1
            if counter == len_list - n:
                if ll.next and ll.next.next:
                    next_node = ll.next.next
                else:
                    next_node = None
                ll.next = next_node
            ll = ll.next
        
        return head
