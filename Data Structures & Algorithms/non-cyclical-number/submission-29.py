class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            total_s= 0
            while n >0:
                last_digit = n % 10
                total_s += last_digit * last_digit
                n = n // 10
            n = total_s

        return n == 1 