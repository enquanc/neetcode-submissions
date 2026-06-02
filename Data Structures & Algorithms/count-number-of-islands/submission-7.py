class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island = 0
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions =  [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(n) and 
                        c in range(m) and 
                        grid[r][c] == '1' and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))



        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    island += 1

        return island
