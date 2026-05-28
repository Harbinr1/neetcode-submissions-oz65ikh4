class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i,v in enumerate(nums):
            comp = target - v
            if comp in map:
                return [map[comp],i]
            
            map[v] = i
        