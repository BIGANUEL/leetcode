from collections import defaultdict

class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)

        # Build graph: a -> b means a is richer than b
        for a, b in richer:
            graph[b].append(a)

        ans = [-1] * n

        def dfs(x):
            # If already computed, return it
            if ans[x] != -1:
                return ans[x]
            
            # Start assuming x is the quietest
            quietest = x
            for richer_person in graph[x]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[quietest]:
                    quietest = candidate
            ans[x] = quietest
            return quietest

        # Run DFS for every person
        for i in range(n):
            dfs(i)
        
        return ans
