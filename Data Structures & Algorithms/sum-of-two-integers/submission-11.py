class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        while b != 0:
            old_a = a
            a = (a^b) & 0xFFFFFFFF
            b = ((old_a & b) << 1) & 0xFFFFFFFF
        
        if a >= 2**31:
            a -= 2**32
        return a
        