from collections import defaultdict, deque

class Solution:
    def isPrintable(self, targetGrid):
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()
        bounds = {}  # color -> [min_row, max_row, min_col, max_col]

        # Step 1: Find bounding rectangles
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                colors.add(c)
                if c not in bounds:
                    bounds[c] = [i, i, j, j]
                else:
                    bounds[c][0] = min(bounds[c][0], i)
                    bounds[c][1] = max(bounds[c][1], i)
                    bounds[c][2] = min(bounds[c][2], j)
                    bounds[c][3] = max(bounds[c][3], j)

        # Step 2: Build dependency graph
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for c in colors:
            r1, r2, c1, c2 = bounds[c]
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if targetGrid[i][j] != c:
                        if targetGrid[i][j] not in graph[c]:
                            graph[c].add(targetGrid[i][j])
                            indegree[targetGrid[i][j]] += 1

        # Step 3: Topological sort
        queue = deque([c for c in colors if indegree[c] == 0])
        printed = 0
        while queue:
            c = queue.popleft()
            printed += 1
            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return printed == len(colors)
