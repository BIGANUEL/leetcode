class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        result = int(dividend / divisor)
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
