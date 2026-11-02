class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0] * (n+1)
        suf = [0] * (n+1)

        for i, h in enumerate(height):
            pre[i+1] = max(pre[i],h)

        for i in range(n-1,-1,-1):
            suf[i] = max(suf[i+1],height[i])

        total_water = 0

        for i, h in enumerate(height):
            total_water += max(min(pre[i],suf[i]) - h,0)        

        return total_water