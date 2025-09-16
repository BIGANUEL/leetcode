class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
            
        count1 = Counter(pattern)
        count2 = Counter(s)

        return len(count1) == len(count2) and len(set(zip(pattern, s))) == len(count1)