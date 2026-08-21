class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for num,freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        