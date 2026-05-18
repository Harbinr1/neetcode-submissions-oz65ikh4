class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            total_sum = 0
            while n > 0:
                last_digits = n % 10
                total_sum += last_digits * last_digits
                n = n // 10
            n = total_sum
        return n == 1
        