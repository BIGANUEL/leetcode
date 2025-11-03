from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0/1 are colors

        for start in range(n):
            if color[start] == -1:
                queue = deque([start])
                color[start] = 0  # assign initial color

                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if color[nei] == -1:
                            color[nei] = 1 - color[node]
                            queue.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True
