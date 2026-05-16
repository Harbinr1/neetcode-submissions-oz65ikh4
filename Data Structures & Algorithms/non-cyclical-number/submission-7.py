class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited and n != 0:
            visited.add(n)
            total_sum = 0

            while n >0 :
                last_digit = n % 10
                total_sum += last_digit * last_digit
                n = n // 10
            
            n = total_sum
        return n ==1