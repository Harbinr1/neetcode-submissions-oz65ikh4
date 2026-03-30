class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index,value in enumerate(nums):
            compliment = target - value
            if compliment in hashMap:
                return [hashMap[compliment],index]
            hashMap[value] = index
        