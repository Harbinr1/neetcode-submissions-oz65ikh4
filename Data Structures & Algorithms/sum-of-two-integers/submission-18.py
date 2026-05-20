class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        carry = 0
        while b !=0:
            old_a = a
            old_b = b
            new = (old_a ^ old_b) & 0xFFFFFFFF
            carry = ((old_a & old_b) << 1) & 0xFFFFFFFF

            a = new
            b = carry

        if a >= 2**31:
            a -= 2**32
        return a