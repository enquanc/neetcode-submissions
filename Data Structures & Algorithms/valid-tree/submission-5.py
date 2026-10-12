from collections import defaultdict 
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nb in graph[node]:
                if nb == parent:
                    continue            # 來的方向，跳過
                elif nb in visited:
                    return False    # 走過且不是parent，為環
                if not dfs(nb, node): # 如果觸發上面的False
                    return False
            # 如果都沒有觸發上面的False，都沒有環
            return True

        # 起點開始並不給parent
        return dfs(0, -1) and (n - 1) == len(edges) and len(visited) == n

