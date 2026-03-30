from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict()
        result = []
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else: 
                frequencies[num] = 1
        
        for _ in range(k):
            max_num = max(frequencies,key = frequencies.get)
            result.append(max_num)
            frequencies.pop(max_num)
        return result
        