# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        lower = float('-inf')
        upper = float('inf')
        queue = deque([(root, lower, upper)])

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node, lower, upper = queue.popleft()
                if node.val <= lower or node.val >= upper:
                    return False

                if node.left:
                    queue.append((node.left, lower, node.val))
                
                if node.right:                
                    queue.append((node.right, node.val, upper))
        return True 
                    