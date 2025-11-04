from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        prereqs = [set() for _ in range(numCourses)]
        
        def dfs(u):
            if prereqs[u]:
                return prereqs[u]
            for v in graph[u]:
                prereqs[u].add(v)
                prereqs[u].update(dfs(v))
            return prereqs[u]

        for i in range(numCourses):
            dfs(i)
        
        return [v in prereqs[u] for u, v in queries]
