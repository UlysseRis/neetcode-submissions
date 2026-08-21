class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        r = n-1
        res = 0
        while l < r:
            res = max(min(heights[r], heights[l]) * (r-l), res)
            if heights[l] < heights[r]:
                l +=1
            else:
                 r-=1
        return res