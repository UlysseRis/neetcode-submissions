class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            s = 0
            for x in piles:
                s += (x + mid - 1) // mid
                if s > h:
                    break

            if s <= h:
                r = mid
            else:
                l = mid + 1

        return l