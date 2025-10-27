class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target):
            if not s and target == 0:
                return True
            for i in range(1, len(s) + 1):
                if can_partition(s[i:], target - int(s[:i])):
                    return True
            return False
        
        ans = 0
        for i in range(1, n + 1):
            sq = i * i
            if can_partition(str(sq), i):
                ans += sq
        return ans
