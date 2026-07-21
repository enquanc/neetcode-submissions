# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # 1. 處理邊界條件：如果樹是空的，直接回傳空陣列
        if not root:
            return []

        # 2. 初始化：準備最終要回傳的陣列，以及用來做 BFS 的 Queue
        result = []
        queue = deque([root])  # 一開始先把根節點放進去

        # 3. 開始 BFS：只要 Queue 裡面還有節點，代表還沒遍歷完
        while queue:
            # 取得「當前這層」的節點數量
            level_size = len(queue) 
            
            # 準備一個暫存陣列，用來裝「當前這層」的所有節點值
            current_level = []

            # 4. 根據當前層的數量跑 for 迴圈
            for _ in range(level_size):
                # 把 Queue 最前面的節點拿出來
                node = queue.popleft()
                
                # TODO: 把拿出來的 node 的值 (node.val) 加進 current_level 中
                current_level.append(node.val)
                # TODO: 如果這個 node 有左子節點 (node.left)，把它加進 Queue 裡等待下一輪處理
                if node.left:
                    queue.append(node.left)

                # TODO: 如果這個 node 有右子節點 (node.right)，也把它加進 Queue 裡
                if node.right:
                    queue.append(node.right)
            
            # 當層迴圈結束，把這層的結果加到最終的 result 裡
            result.append(current_level)

        # 回傳最終結果
        return result