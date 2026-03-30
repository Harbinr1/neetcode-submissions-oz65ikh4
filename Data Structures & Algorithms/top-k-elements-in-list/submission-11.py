from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = defaultdict(int)

        freq = [[] for i in range(len(nums) + 1)]

        for index,val in enumerate(nums):
            countFreq[val] += 1
        

        for num,freq_val in countFreq.items():
            freq[freq_val].append(num)

        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return list(res)


