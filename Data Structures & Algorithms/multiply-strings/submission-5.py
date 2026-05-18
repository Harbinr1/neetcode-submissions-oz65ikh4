class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_map = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        
        val1 = 0
        for char in num1:
            val1 = val1 * 10 + digit_map[char]
        
        val2 = 0
        for char in num2:
            val2 = val2 * 10 + digit_map[char]
        
        total = val1*val2

        return str(total)

        

        