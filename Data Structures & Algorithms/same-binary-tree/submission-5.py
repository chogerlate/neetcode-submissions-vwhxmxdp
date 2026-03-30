# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # let use iterative approach
        visited_p, visited_q = [], []
        def pre_order(root, visited):
            if not root :
                visited.append(None) 
                return None
            visited.append(root.val)
            pre_order(root.left,visited)
            pre_order(root.right, visited)

        pre_order(p, visited_p)
        pre_order(q, visited_q)
        
        

        return True if visited_p == visited_q else False