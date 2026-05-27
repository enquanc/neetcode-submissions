from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. 準備裝備：預先算好小於等於 n 的完全平方數，由大到小或由小到大皆可
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        
        # 2. 準備 Queue，裡面放 Tuple: (目前的數字, 累積的步數)
        # 起點是數字 n，目前走了 0 步
        queue = deque([(n, 0)])
        
        # 3. 準備 Visited Set，用來記錄「已經走過的數字」，避免重複計算 (避免超時的關鍵)
        visited = set()
        visited.add(n)
        
        # 開始 BFS 一層層尋找最短路徑
        while queue:
            # 拿出 Queue 最前面的狀態
            current_num, steps = queue.popleft()
            
            # 嘗試走下一步 (減去各個平方數)
            for square in squares:
                # 計算下一步剩下的數字
                next_num = current_num - square
                
                # 4. 終止條件：如果剛好減到 0，代表我們走到終點了！
                if next_num == 0:
                    # TODO: 既然已經走到 0 了，我們應該回傳什麼？(提示：與目前的步數有關)
                    return steps + 1
                
                # 5. 繼續探索：如果數字還大於 0，且這個數字以前沒遇過
                if next_num > 0 and next_num not in visited:
                    # TODO: 把「下一步的數字」和「更新後的步數」打包成 Tuple 加進 Queue 中
                    queue.append((next_num, steps+1)) 
                    
                    # TODO: 把這個新的數字標記為已走過，放進 Set 裡面
                    visited.add(current_num) 
                    
        return -1 # 理論上一定找得到答案，不會走到這行