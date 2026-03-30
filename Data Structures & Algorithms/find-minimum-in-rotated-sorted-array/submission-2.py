class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] <= nums[hi]:
                hi = mid
        return nums[lo]
        