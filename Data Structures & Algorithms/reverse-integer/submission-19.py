class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31-1
        is_negative = x < 0

        reversed_res = 0
        x = abs(x)
        while x > 0:
            if reversed_res > MAX // 10:
                return 0 
            
            else:
                last_digit = x % 10
                reversed_res = (reversed_res * 10) + last_digit
                x = x // 10
        
        if is_negative:
            return -reversed_res
        
        return reversed_res