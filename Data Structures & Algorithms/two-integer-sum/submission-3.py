class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,val in enumerate(nums):
            compliment = target - val
            if compliment in hashmap:
                return [hashmap[compliment],index]
            hashmap[val] = index
        return []