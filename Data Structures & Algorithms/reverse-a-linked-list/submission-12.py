# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversal_target = None
        current_redirect_node, next_redirect_node = head, head

        while current_redirect_node is not None :
            # 1: move the next_redirect_node to the next node
            next_redirect_node = next_redirect_node.next
            # 2: redirect the current_redirect_node.next to the reversal_target
            current_redirect_node.next = reversal_target
            # 3: move the reversal target to the current node to prepare for next iteration
            reversal_target = current_redirect_node
            # 4: mvoe the current_redirect_node to the next redirect target in next_redirect_node
            current_redirect_node = next_redirect_node
        
        return reversal_target 