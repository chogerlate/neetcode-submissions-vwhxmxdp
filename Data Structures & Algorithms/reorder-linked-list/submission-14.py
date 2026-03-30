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
        if not head or not head.next : return
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
        
        def findMid(root):
            fast, slow = root, root
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            
            return slow # the middle part
        
        mid_node = findMid(head)
        second_half = reverse(mid_node.next)
        mid_node.next = None
        cur_second_half = second_half
        cur_first_half = head
        while cur_second_half :
            link_first_half, link_second_half = cur_first_half.next, cur_second_half.next
            cur_first_half.next = cur_second_half
            cur_second_half.next = link_first_half
        
            cur_second_half = link_second_half
            cur_first_half = link_first_half


            