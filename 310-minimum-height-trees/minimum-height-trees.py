from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]  # single node case

        # Build adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Initialize leaves (nodes with one connection)
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])

        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()
                # remove leaf from its neighbor
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                # if neighbor became a leaf, enqueue it
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        # remaining nodes are centers
        return list(leaves)
