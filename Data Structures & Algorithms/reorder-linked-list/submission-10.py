# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        This possibly use 3 pointers approach 
        start small
        [0,1,2] : 0 -> 1 -> 2 -> None
        Process:
            
        [0,2,1] : 0 -> 2 -> 1 -> None

        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        def reverse(root):
            reversal_head = None
            cur_head, next_head = root, root
            while cur_head:
                next_head = next_head.next
                cur_head.next = reversal_head
                reversal_head = cur_head
                cur_head = next_head
            return reversal_head
        
        cur_head = head
        while cur_head :
            cur_head.next = reverse(cur_head.next)
            cur_head = cur_head.next
        



            