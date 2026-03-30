class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        first = 0
        nums.sort()
        while first <= len(nums) -3:
            if first > 0 and nums[first] == nums[first - 1]:
                first += 1
                continue
            left = first + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[first] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                        left += 1
                    
                else:
                    res.append([nums[first],nums[left],nums[right]])
                    

                    while left < right and nums[left] == nums[left +1]:
                        left += 1
                    left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                     
                
            first += 1
        return res

