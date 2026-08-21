class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            val = nums[i]

            if val > 0:
                break

            if i > 0 and val == nums[i - 1]:
                continue

            if val + nums[n - 1] + nums[n - 2] < 0:
                continue

            if val + nums[i + 1] + nums[i + 2] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                s = val + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res