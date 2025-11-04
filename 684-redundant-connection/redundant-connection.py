class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(n+1)]  # nodes are 1-based

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            union(u, v)
