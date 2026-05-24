class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        res = []


        for num in nums:
            map[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for freq,val in map.items():
            bucket[val].append(freq)
        
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
