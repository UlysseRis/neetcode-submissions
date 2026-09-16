class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = float("inf")
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < minimum:
                minimum = nums[mid]

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return minimum      