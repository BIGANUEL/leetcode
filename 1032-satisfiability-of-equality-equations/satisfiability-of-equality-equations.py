class Solution:
    def equationsPossible(self, equations):
        parent = [i for i in range(26)]  # for 'a' to 'z'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Process all "==" equations
        for eq in equations:
            if eq[1:3] == "==":
                a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                union(a, b)

        # Step 2: Process all "!=" equations
        for eq in equations:
            if eq[1:3] == "!=":
                a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
                if find(a) == find(b):
                    return False

        return True
