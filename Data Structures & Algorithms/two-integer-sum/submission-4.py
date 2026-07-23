class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {x: i for i, x in enumerate(nums)}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in d and i != d[target - nums[i]]:
                return [i,d[target - nums[i]]] 
        