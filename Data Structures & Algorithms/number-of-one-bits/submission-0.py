class Solution:
    def hammingWeight(self, n: int) -> int:
        one_count = 0
        while n:
            if n & 1:
                one_count += 1
            n = n >> 1
        return one_count
        