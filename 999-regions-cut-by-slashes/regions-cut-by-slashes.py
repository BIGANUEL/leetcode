class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                # Unique id for each triangle
                root = (i * n + j) * 4
                val = grid[i][j]
                # Connect triangles inside the cell
                if val == '/':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif val == '\\':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:  # ' '
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)

                # Connect with right cell
                if j + 1 < n:
                    union(root + 1, ((i * n + (j+1)) * 4) + 3)
                # Connect with bottom cell
                if i + 1 < n:
                    union(root + 2, (((i+1) * n + j) * 4) + 0)

        # Count unique parents
        return len({find(x) for x in parent})
