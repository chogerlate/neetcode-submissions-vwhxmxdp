# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Ask the left and right subtrees for their height
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        # My height is 1 (myself) + the tallest child
        return 1 + max(left_height, right_height)