class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        maxLen = 0
        for n in nums:
            hashset.add(n)
        

        for n in nums:
            if n-1 not in hashset:
                cur_num = n
                cur_len = 1
                while cur_num + 1 in hashset:
                    cur_num += 1
                    cur_len += 1
                
                maxLen = max(maxLen,cur_len)
        return maxLen