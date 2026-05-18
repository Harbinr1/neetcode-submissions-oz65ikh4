class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_char = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        val1 = 0
        for char in num1:
            val1 = val1 * 10 + digit_char[char]
        
        val2 = 0
        for char in num2:
            val2 = val2 * 10 + digit_char[char]
        

        total = val1 * val2
        if total == 0:
            return '0'
        res = []
        while total > 0:
            digit = total % 10
            res.append(chr(digit + ord('0')))
            total //= 10
        
        
        
        res_str = "".join(res[::-1])
        return res_str

