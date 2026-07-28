# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                break
        
        root_node = TreeNode(root_val)

        left_in = inorder[:i]
        right_in = inorder[i+1:]

        left_pre = preorder[1:i+1]
        right_pre = preorder[i+1:]

        root_node.left = self.buildTree(left_pre, left_in)
        root_node.right = self.buildTree(right_pre, right_in)

        return root_node



        