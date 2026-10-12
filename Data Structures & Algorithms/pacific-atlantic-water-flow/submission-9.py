from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    new_r, new_c = r + dr, c + dc
                    # 在邊界內
                    if (0 <= new_r < m and 0 <= new_c < n 
                    and (new_r, new_c) not in visited  # 確認沒走過
                    and heights[new_r][new_c] >= heights[r][c]
                    ): 
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
            return visited
        
        pacific_starts  = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]    
        # 第一列 + 第一行
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]   
        # 最後一列 + 最後一行

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)
        return [list(p) for p in pac & atl]