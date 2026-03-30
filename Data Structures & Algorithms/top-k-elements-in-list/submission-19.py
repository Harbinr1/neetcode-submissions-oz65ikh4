from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        freq = [[] for _ in range(len(nums)+ 1)]

        for num in nums:
            hashMap[num] += 1
        

        for index,freq_val in hashMap.items():
            freq[freq_val].append(index)
        
        res = []
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


