# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0      # 記錄目前走訪了幾個節點
        result = None  # 記錄最終的答案

        def inorder(node):
            # 宣告我們要修改的是外層 (kthSmallest) 的變數
            nonlocal count, result
            
            # 如果節點為空，或者已經找到答案了(提前結束)，就返回
            if not node or result is not None:
                return
            
            # 1. 往左子樹走到底
            inorder(node.left)
            
            # 2. 處理當前節點 (中序)
            count += 1
            if count == k:
                result = node.val
                return  # 找到答案，開始回傳
            
            # 3. 往右子樹走
            inorder(node.right)
            
        # 啟動遞迴
        inorder(root)
        return result