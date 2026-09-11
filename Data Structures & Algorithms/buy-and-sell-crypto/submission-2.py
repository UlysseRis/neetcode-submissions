class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0 
        r = 1
        profit = 0
        while r < n:
            profit = max(profit, prices[r]-prices[l])
            if prices[r] <= prices[l]:
                l = r
            r +=1
        return profit

