class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        if not nums:
            return 0
        
        numbers = set(nums)
        for num in numbers:
            if num - 1 not in numbers:
                current = num
                length = 1

                while current + 1 in numbers:
                    current += 1
                    length += 1
                
                max_length  = max(max_length,length)
        return max_length
            




        