# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head_a, head_b = list1, list2
        # Edge case
        if not head_a : return head_b
        if not head_b : return head_a

        dummy_head = ListNode(-1) # this will use as achore for our merged linked list
        cur_head = dummy_head
        while head_a and head_b :
            if head_a.val < head_b.val:
                cur_head.next = head_a
                head_a = head_a.next
            else:
                cur_head.next = head_b
                head_b = head_b.next
            
            cur_head = cur_head.next
        
        # remaining node 
        if head_a : cur_head.next = head_a
        if head_b : cur_head.next = head_b

        return dummy_head.next