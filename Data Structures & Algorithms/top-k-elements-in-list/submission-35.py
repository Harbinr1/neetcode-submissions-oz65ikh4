class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        

        bucket = [[] for _ in range(len(nums)+1)]

        for val,freq in map.items():
            bucket[freq].append(val)
        
        res = []
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
                    
        