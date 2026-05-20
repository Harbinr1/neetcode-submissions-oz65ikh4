class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        while b != 0:
            old_a = ((a ^ b) & 0xFFFFFFFF)
            b = (a & b) << 1 & 0xFFFFFFFF

            a = old_a
        
        if a >= 2 ** 31:
             a-= 2**32
        return a