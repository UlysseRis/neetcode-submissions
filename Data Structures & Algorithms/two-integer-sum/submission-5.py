class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {x: i for i, x in enumerate(nums)}

        for i, x in enumerate(nums):
            j = d.get(target - x)
            if j is not None and j != i:
                return [i, j]
        