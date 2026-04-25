# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(q,p):
            if not q and not p:
                return True
            if not q or not p or p.val != q.val:
                return False
            return sameTree(q.left,p.left) and sameTree(q.right,p.right) 

        if subRoot == None:
            return True
        if root == None:
            return False
        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

