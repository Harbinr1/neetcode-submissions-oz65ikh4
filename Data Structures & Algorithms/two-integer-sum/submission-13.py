class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i,v in enumerate(nums):
            cmp = target - v
            if cmp in map:
                return [map[cmp],i]
            map[v] = i
        