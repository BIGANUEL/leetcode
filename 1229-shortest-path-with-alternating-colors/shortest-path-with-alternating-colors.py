from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        # Build adjacency lists
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        # Result distances initialized to infinity
        dist = [float('inf')] * n
        dist[0] = 0
        
        # BFS Queue: (node, color)
        # color: 0 = red, 1 = blue
        q = deque()
        q.append((0, 0))  # red
        q.append((0, 1))  # blue
        
        # Visited set to prevent revisiting (node, color)
        visited = [[False, False] for _ in range(n)]
        visited[0][0] = visited[0][1] = True
        
        steps = 0
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                dist[node] = min(dist[node], steps)
                
                # Determine next color (alternate)
                next_color = 1 - color
                next_adj = blue_adj if color == 0 else red_adj
                
                for nei in next_adj[node]:
                    if not visited[nei][next_color]:
                        visited[nei][next_color] = True
                        q.append((nei, next_color))
            steps += 1
        
        # Replace unreachable nodes with -1
        return [d if d != float('inf') else -1 for d in dist]
