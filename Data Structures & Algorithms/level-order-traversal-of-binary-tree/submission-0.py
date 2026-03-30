# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        3-tree framework
        1: top-down
        2: add node the the queue for bfs, 
        3: basecase: return None
        """
        if not root : return []
        queue = deque([root])
        res = []
        while queue:
            counter = len(queue)
            current_level = []
            for _ in range(counter):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left : 
                    queue.append(node.left)
                if node.right : 
                    queue.append(node.right)
            res.append(current_level)
        return res