MOD = 10**9 + 7

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

class Solution:
    def createSortedArray(self, instructions):
        max_val = max(instructions)
        bit = Fenwick(max_val + 2)
        cost = 0
        
        for i, x in enumerate(instructions):
            less = bit.query(x - 1)
            greater = i - bit.query(x)
            cost += min(less, greater)
            cost %= MOD
            bit.update(x, 1)
        
        return cost % MOD
