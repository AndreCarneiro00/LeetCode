# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summed_initial_val = l1.val + l2.val
        initial_val = summed_initial_val - 10 if summed_initial_val > 9 else summed_initial_val
        new_list_head = ListNode(initial_val)
        new_list = new_list_head
        l1 = l1.next
        l2 = l2.next
        add_one = True if summed_initial_val > 9  else False
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_value = l1_val + l2_val + add_one
            add_one = False
            if new_value > 9:
                new_value = new_value - 10
                add_one = True
            
            new_node = ListNode(new_value)
            new_list.next = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            new_list = new_list.next
        
        if add_one:
            new_list.next = ListNode(1)

        return new_list_head