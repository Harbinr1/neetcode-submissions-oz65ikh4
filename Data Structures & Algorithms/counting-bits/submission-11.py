class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(n):
            ones = 0
            while n:
                if n & 1:
                    ones += 1
                n = n >> 1
            return ones
        output = [0] * (n + 1)

        for i in range(len(output)):
            output[i] = countOnes(i)
        return output
        