class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nb in graph[node]:
                dfs(nb)
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count