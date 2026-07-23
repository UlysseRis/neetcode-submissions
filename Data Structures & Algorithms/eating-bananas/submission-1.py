class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        if h == len(piles):
            return maxk
        l = 1
        r = maxk
        while l<=r:
            mid=(l+r)//2
            s = 0
            for x in piles:
                s += (x + mid - 1) // mid
            if s<=h:
                r = mid-1
            else:
                l = mid + 1
        return l
        