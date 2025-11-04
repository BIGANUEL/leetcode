from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        
        # Map each character to all its positions in ring
        positions = defaultdict(list)
        for i, ch in enumerate(ring):
            positions[ch].append(i)
        
        @lru_cache(None)
        def dfs(i, pos):
            # Base case: all characters in key are done
            if i == len(key):
                return 0
            
            res = float('inf')
            for nxt in positions[key[i]]:
                # Distance between current position and target
                diff = abs(pos - nxt)
                step = min(diff, n - diff)  # rotate either direction
                # +1 for pressing the button
                res = min(res, step + 1 + dfs(i + 1, nxt))
            return res
        
        return dfs(0, 0)
