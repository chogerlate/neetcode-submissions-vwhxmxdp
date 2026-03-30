# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case: If the main tree is empty, we can't find anything
        if not root: 
            return False
        
        # 1. Check if the trees are IDENTICAL starting here
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. If not, look in the left and right children
        # We use OR because if it's found in either side, we win.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, t):
        # The classic template:
        if not s and not t: return True
        if not s or not t or s.val != t.val: return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
